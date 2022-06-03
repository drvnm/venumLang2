from typing import List
from parsing.statements import *
from parsing.expressions import *
from intermediate.tokens import *
from intermediate.lookup_tables import *
from scanning.error import *

class TypeEnv:
    def __init__(self):
        self.enclosing = None
        self.variables = {}
        self.functions = {}

    def define_var(self, name: str, type: tokens):
        self.variables[name] = type

    def get_var(self, name: str):
        if name in self.variables:
            return self.variables[name]
        elif self.enclosing is not None:
            return self.enclosing.get_var(name)
        else:
            return None
    
    def define_func(self, name: str, type: tokens):
        self.functions[name] = type
    
    def get_func(self, name: str):
        if name in self.functions:
            return self.functions[name]
        elif self.enclosing is not None:
            return self.enclosing.get_func(name)
        else:
            return None
        
    def set_enclosing(self, enclosing: 'TypeEnv'):
        self.enclosing = enclosing


# takes in a series of statements and checks if they are valid
class TypeChecker:
    def __init__(self, statements: List[Stmt]):
        self.statements = statements
        self.errors = []


        self.type_stack = []

        # type info about variables and functions
        self.env = TypeEnv()
        self.globals = self.env

    def execute(self):
        for statement in self.statements:
            self.visit(statement)

    def visit(self, statement):
        statement.accept(self)

    def visit_literal_expr(self, expr: LiteralExpr):
        self.type_stack.append(expr.type)
    
    def visit_var_expr(self, expr: VarExpr):
        type = self.env.get_var(expr.name.lexeme)
        self.type_stack.append(type)
    
    def visit_unary_expr(self, expr: UnaryExpr):
        self.visit(expr.right)
        type = self.type_stack.pop()
        if type not in acceptable_types[tokens.INT]:
            error(expr.right.value,
                  f"""Type {type} is not valid for unary expression with operator {expr.operator.lexeme}""")
        else:
            self.type_stack.append(tokens.INT)

    def visit_binary_expr(self, expr: BinaryExpr):
        self.visit(expr.left)
        self.visit(expr.right)

        left_type = self.type_stack.pop()
        right_type = self.type_stack.pop()

        if left_type not in arithmetic_tokens or left_type not in arithmetic_tokens:
            error(expr.left.value,
                  f"""Operands of binary expression with operator {expr.operator.lexeme} must be integral, got types {left_type} and {right_type}""")
        else:
            self.type_stack.append(tokens.INT)
    
    def visit_var_stmt(self, var_stmt: VarStmt):
        if var_stmt.expr: # if the variable has an initializer
            self.visit(var_stmt.expr)
            initializer_type = self.type_stack.pop()
            if initializer_type not in acceptable_types[var_stmt.type.type]:
                error(var_stmt.name,
                      f"""Type {initializer_type} is not valid for variable of type {var_stmt.type.type}""")
        self.env.define_var(var_stmt.name.lexeme, var_stmt.type.type)
    
    def visit_assignment_expr(self, assignment_expr: AssignmentExpr):
        original_type = self.env.get_var(assignment_expr.name.lexeme)
        self.visit(assignment_expr.value)
        value_type = self.type_stack.pop()
        if value_type not in acceptable_types[original_type]:
            error(assignment_expr.name,
                  f"""Type {value_type} is not valid for assignment expression (exptected {original_type})""")
    
    def execute_block(self, block: BlockStmt, env: TypeEnv):
        new_env = TypeEnv()
        new_env.set_enclosing(env)
        old_env = self.env
        self.env = new_env

        for statement in block.statements:
            self.visit(statement)

        self.env = old_env

    def visit_expr_stmt(self, expr_stmt: ExprStmt):
        self.visit(expr_stmt.expr)

    def visit_print_stmt(self, print_stmt: PrintStmt):
        self.visit(print_stmt.expr)
        type = self.type_stack.pop()
        if type not in acceptable_types[tokens.INT]:
            error("Oops",
                  f"""Type {type} is not valid for print statement""")

    def visit_syscall_stmt(self, syscall_stmt: SyscallStmt):
        for expr in syscall_stmt.args:
            self.visit(expr)
            type = self.type_stack.pop()
            if type not in acceptable_types[tokens.INT]:
                error(expr.value,
                      f"""Type {type} is not valid for syscall statement""")
        
    def visit_if_stmt(self, if_stmt: IfStmt):
        self.visit(if_stmt.condition)
        condition_type = self.type_stack.pop()
        if condition_type != tokens.INT:
            error(if_stmt.condition.value,
                  f"""Type {condition_type} is not valid for if statement condition""")
        for statement in if_stmt.elif_statements:
            cond = statement[0]
            branch = statement[1]
            self.visit(cond)
            condition_type = self.type_stack.pop()
            if condition_type not in acceptable_types[tokens.INT]:
                error(cond.value,
                      f"""Type {condition_type} is not valid for if statement condition""")
            self.visit(branch)
        if if_stmt.else_branch:
            self.visit(if_stmt.else_branch)
    
    def visit_while_stmt(self, while_stmt: WhileStmt):
        self.visit(while_stmt.condition)
        condition_type = self.type_stack.pop()
        if condition_type != tokens.INT:
            error(while_stmt.condition.value,
                  f"""Type {condition_type} is not valid for while statement condition""")
        self.visit(while_stmt.body)

    def visit_block_stmt(self, block_stmt: BlockStmt):
        new_env = TypeEnv()
        self.execute_block(block_stmt, new_env)
    
    def visit_func_stmt(self, func_stmt: FuncStmt):
        self.globals.define_func(func_stmt.name.lexeme, func_stmt)
        new_env = TypeEnv()
        new_env.set_enclosing(self.globals)

        # define all parameters in the functions env
        for param in func_stmt.parameters:
            new_env.define_var(param.name.lexeme, param.type.type)

        self.execute_block(func_stmt.body, new_env)
        
    def visit_call_expr(self, call_expr: CallExpr):
        str_name = call_expr.callee.name.lexeme
        callee = self.globals.get_func(str_name)
        if callee is None:
            error(call_expr.callee.name,
                  f"""Function {call_expr.callee.lexeme} is not defined""")
        if len(call_expr.arguments) != len(callee.parameters):
            error(call_expr.callee.name,
                  f"""Function {str_name} expected {len(callee.parameters)} argument(s), got {len(call_expr.arguments)}""")

        for (arg, param) in zip(call_expr.arguments, callee.parameters):
            self.visit(arg)
            arg_type = self.type_stack.pop()
            if arg_type not in acceptable_types[param.type.type]:
                error(call_expr.callee.name,
                      f"""Type {arg_type} is not valid for argument of function {str_name}""")
        self.type_stack.append(callee.return_type)