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