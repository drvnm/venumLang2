from abc import ABC, abstractmethod
from typing import List
from .expressions import *

class Stmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# represents a print statement like print <expr>;
class PrintStmt(Stmt):
    def __init__(self, expr: Expr):
        self.expr = expr
    
    def accept(self, visitor):
        visitor.visit_print_stmt(self)
    
# represents any expression that has side effect
class ExprStmt(Stmt):
    def __init__(self, expr: Expr):
        self.expr = expr
    
    def accept(self, visitor):
        visitor.visit_expr_stmt(self)

# represents a variable declaration like var x = <expr>;
class VarStmt(Stmt):
    def __init__(self, type: tokens, name: Token, expr: Expr, size: int):
        self.type = type
        self.name = name
        self.expr = expr
        self.size = size
    
    def accept(self, visitor):
        visitor.visit_var_stmt(self)

# represents a block of statements
class BlockStmt(Stmt):
    def __init__(self, statements: List[Stmt]):
        self.statements = statements

    def accept(self, visitor):
        visitor.visit_block_stmt(self)

# class that represents if statement, with elifs and else statements
class IfStmt(Stmt):
    def __init__(self, condition: Expr, then_branch: Stmt, elif_statements: List[Stmt], else_branch: Stmt):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
        self.elif_statements = elif_statements
    
    def accept(self, visitor):
        visitor.visit_if_stmt(self)

# class to represent while statements
class WhileStmt(Stmt):
    def __init__(self, condition: Expr, body: Stmt, label_index: int, end_index: int):
        self.condition = condition
        self.body = body
        self.label_index = label_index
        self.end_index = end_index
    
    def accept(self, visitor):
        visitor.visit_while_stmt(self)