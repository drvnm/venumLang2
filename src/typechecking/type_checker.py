from typing import List
from parsing.statements import *
from parsing.expressions import *
from intermediate.tokens import *
from intermediate.lookup_tables import *
from scanning.error import *

# takes in a series of statements and checks if they are valid


class TypeChecker:
    def __init__(self, statements: List[Stmt]):
        self.statements = statements
        self.errors = []

        self.type_stack = []

    def execute(self):
        for statement in self.statements:
            self.visit(statement)

    def visit(self, statement):
        statement.accept(self)

    def visit_literal_expr(self, expr: LiteralExpr):
        self.type_stack.append(expr.type)

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


    def visit_expr_stmt(self, expr_stmt: ExprStmt):
        self.visit(expr_stmt.expr)

    def visit_print_stmt(self, print_stmt: PrintStmt):
        self.visit(print_stmt.expr)
        type = self.type_stack.pop()
        if type not in acceptable_types[tokens.INT]:
            error(print_stmt.expr.value,
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

    def visit_block_stmt(self, block_stmt: BlockStmt):
        for statement in block_stmt.statements:
            self.visit(statement)