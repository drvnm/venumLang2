from abc import ABC, abstractmethod
from typing import List
from intermediate.tokens import *
from visitors.visitor import ExprVisitor


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

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_binary_expr(self)

# this class represents an expression like ( <expr> )


class GroupingExpr(Expr):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_grouping_expr(self)

# this class represents an expression like 2.3 or "my string"


class LiteralExpr(Expr):
    def __init__(self, value: Token):
        self.value = value

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_literal_expr(self)

# this class represents an expression like !true


class UnaryExpr(Expr):
    def __init__(self, operator: tokens, right: Expr):
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_unary_expr(self)

# class to represent variable expressions like x


class VarExpr(Expr):
    def __init__(self, name: Token):
        self.name = name

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_var_expr(self)

# class to represent a variable to pointer expression like &x


class VarToPointerExpr(Expr):
    def __init__(self, name: Token):
        self.name = name

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_var_to_pointer_expr(self)

# class to represent a dereference expression like *x


class DereferenceExpr(Expr):
    def __init__(self, expr: Expr):
        self.expr = expr

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_dereference_expr(self)

# class to represent assignment expression like x = 2


class AssignmentExpr(Expr):
    def __init__(self, name: Token, operator: tokens, value: Expr, mode: str = "var", index: Expr = 0):
        self.operator = operator
        self.name = name
        self.value = value
        self.mode = mode
        self.index = index

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_assignment_expr(self)

# class to represent a function call expression like f(x, y)


class CallExpr(Expr):
    def __init__(self, callee: VarExpr, arguments: List[Expr]):
        self.callee = callee
        self.arguments = arguments

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_call_expr(self)

# represesnts accesing an array element


class ArrayAccessExpr(Expr):
    def __init__(self, name: tokens, index: Expr):
        self.name = name
        self.index = index

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_array_access_expr(self)
