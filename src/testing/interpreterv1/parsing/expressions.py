from abc import ABC, abstractmethod
from visitors.visitor import Visitor
from intermediate.tokens import *


class Expr(ABC):
    @abstractmethod
    def accept(self, visitor): ...



class BinaryExpr(Expr):  # defines binary expressions, like 3 + 2
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor: Visitor):
        return visitor.visit_binary_expression(self)


class GroupingExpr(Expr):  # defines groupings like (3 + 2)
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: Visitor):
        return visitor.visit_grouping_expression(self)


class LiteralExpr(Expr):  # difines literals like 3 or "hi"
    def __init__(self, value: Token):
        self.value = value

    def accept(self, visitor: Visitor):
        return visitor.visit_literal_expression(self)


class UnaryExpr(Expr):  # defines unary expressions like !true
    def __init__(self, operator: Token, right: Expr):
        self.operator = operator
        self.right = right

    def accept(self, visitor: Visitor):
        return visitor.visit_unary_expression(self)

class VarExpr(Expr): # defines variable decl
    def __init__(self, name: Token):
        self.name = name
    
    def accept(self, visitor: Visitor):
        return visitor.visit_var_expression(self)
    
class AssignExpr(Expr): # defines variable assignment
    def __init__(self, name: Token, value: Expr):
        self.name = name
        self.value = value
    
    def accept(self, visitor: Visitor):
        return visitor.visit_assign_expression(self)

class LogicalExpr(Expr): # defines logical expressions
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right
    
    def accept(self, visitor: Visitor):
        return visitor.visit_logical_expression(self)