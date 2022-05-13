from abc import ABC, abstractmethod
from typing import List
from visitors.visitor import Visitor
from .expressions import Expr
from intermediate.tokens import *

# class for statements
class StatementVisitor(ABC):
    def visit_print_statement(self, print_statement): ...
    
    def visit_expression_statement(self, expression_statement): ...

    
class Statement(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor): ...
    
    
# class for expressions, like binary ops.
class ExpressionStatement(Statement):
    def __init__(self, expr: Expr):
        self.expr = expr
        
    def accept(self, visitor: Visitor):
        return visitor.visit_expression_statement(self)
    
# class for print statements, like "print" expression
class PrintStatement(Statement):
    def __init__(self, expr: Expr):
        self.expr = expr
        
    def accept(self, visitor: Visitor):
        return visitor.visit_print_statement(self)

class LetStatement(Statement):
    def __init__(self, name: Token, value: Expr):
        self.name = name
        self.value = value
        
    def accept(self, visitor: Visitor):
        return visitor.visit_let_statement(self)

# class for block statements, like  { let x = 3; { print x;}}
class BlockStatement(Statement):
    def __init__(self, statements: List[Statement]):
        self.statements = statements
        
    def accept(self, visitor: Visitor):
        return visitor.visit_block_statement(self)

# class for if statements, like if(3 > 2) {} elseStmt?
class IfStatement(Statement):
    def __init__(self, condition: Expr, then_branch: Statement, else_branch: Statement):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
    
    def accept(self, visitor: Visitor):
        return visitor.visit_if_statement(self)