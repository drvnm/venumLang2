from abc import ABC, abstractmethod
from intermediate.tokens import *
from visitors.visitor import Visitor

# base class for every kind of expression
class Expr(ABC):

    # abstract accpet method which will call the specified visitor method
    @abstractmethod
    def accept(self, visitor): ...

# this class represents an expression like <expr> (+, -, *, /) <expr>
class BinaryExpr(Expr):
    def __init__(self, left: Expr, operator: tokens, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right
    
    def accept(self, visitor: Visitor):
        return visitor.visit_binary_expr(self)

# this class represents an expression like ( <expr> )
class GroupingExpr(Expr):
    def __init__(self, expression: Expr):
        self.expression = expression
    
    def accept(self, visitor: Visitor):
        return visitor.visit_grouping_expr(self)
    
# this class represents an expression like 2.3 or "my string"
class LiteralExpr(Expr):
    def __init__(self, value: Token):
        self.value = value
    
    def accept(self, visitor: Visitor):
        return visitor.visit_literal_expr(self)
    
# this class represents an expression like !true
class UnaryExpr(Expr):
    def __init__(self, operator: tokens, right: Expr):
        self.operator = operator
        self.right = right

    def accept(self, visitor: Visitor):
        return visitor.visit_unary_expr(self)
