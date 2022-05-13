from typing import List
from visitors.visitor import Visitor
from .environment import Environment
from parsing.statements import *
from parsing.expressions import *
from intermediate.tokens import *

class Interpreter(Visitor, StatementVisitor):
    def __init__(self):
        self.environment = Environment()
        
    def execute_block(self, block: BlockStatement, environment: Environment):
        previous = self.environment
        self.environment = environment
        for statement in block.statements:
            self.interpret(statement)
        self.environment = previous
    
    def execute(self, statements: List[Statement]):
        for statement in statements:
            self.interpret(statement)
    
    def interpret(self, expr: Expr): 
        return expr.accept(self)
    
    def visit_literal_expression(self, expr: LiteralExpr):
        return expr.value.literal

    def visit_grouping_expression(self, grouping_expression: GroupingExpr):
        return self.interpret(grouping_expression.expression)

    def visit_unary_expression(self, unary_expression: UnaryExpr):
        right = self.interpret(unary_expression.right)
        if unary_expression.operator.type == tokens.MINUS:
            return -right
        elif unary_expression.operator.type == tokens.BANG:
            return not right
        
    def visit_var_expression(self, var_expr: VarExpr):
        return self.environment.get(var_expr.name.lexeme)
        
    def visit_binary_expression(self, binary_expression: BinaryExpr):
        left = self.interpret(binary_expression.left)
        right = self.interpret(binary_expression.right)
        
        if binary_expression.operator.type == tokens.MINUS:
            return left - right
        elif binary_expression.operator.type == tokens.PLUS:
            # check if left or right is str
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            else:
                return left + right
        elif binary_expression.operator.type == tokens.SLASH:
            return left / right
        elif binary_expression.operator.type == tokens.STAR:
            return left * right
        elif binary_expression.operator.type == tokens.GREATER:
            return left > right
        elif binary_expression.operator.type == tokens.GREATER_EQUAL:
            return left >= right
        elif binary_expression.operator.type == tokens.LESS:
            return left < right
        elif binary_expression.operator.type == tokens.LESS_EQUAL:
            return left <= right
        elif binary_expression.operator.type == tokens.BANG_EQUAL:
            return left != right
        elif binary_expression.operator.type == tokens.EQUAL_EQUAL:
            return left == right
        
    def visit_assign_expression(self, assignment_expression: AssignExpr):
        value = self.interpret(assignment_expression.value)
        self.environment.assign(assignment_expression.name.lexeme, value)
        return value
        
    def visit_expression_statement(self, expression_statement: ExpressionStatement):
        self.interpret(expression_statement.expr)
        return
    
    def visit_print_statement(self, print_statement: PrintStatement):
        value = self.interpret(print_statement.expr)
        print(str(value))
        return
    
    def visit_let_statement(self, let_statement: LetStatement):
        value = self.interpret(let_statement.value) if let_statement.value else None
        self.environment.define(let_statement.name.lexeme, value)
        return
    
    def visit_block_statement(self, block_statement: BlockStatement):
        env = Environment()
        env.set_enclosing_env(self.environment)
        self.execute_block(block_statement, env)
        return
    
    def visit_if_statement(self, if_statement: IfStatement):
        if self.interpret(if_statement.condition):
            self.interpret(if_statement.then_branch)
        elif if_statement.else_branch:
            self.interpret(if_statement.else_branch)
        return
    
    def visit_logical_expression(self, logical_expression: LogicalExpr):
        left = self.interpret(logical_expression.left)
        right = self.interpret(logical_expression.right)
                
        if logical_expression.operator.type == tokens.OR:
            return left or right
        elif logical_expression.operator.type == tokens.AND:
            return left and right