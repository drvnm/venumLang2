from abc import ABC, abstractmethod
from intermediate.tokens import *


class Expr:
    @abstractmethod
    def accept(self, visitor):
        pass


class Visitor(ABC):
    @abstractmethod
    def visit_binary_expression(self, binary_expression: Expr):
        pass

    @abstractmethod
    def visit_grouping_expression(self, grouping_expression: Expr):
        pass

    @abstractmethod
    def visit_literal_expression(self, literal_expression: Expr):
        pass

    @abstractmethod
    def visit_unary_expression(self, unary_expression: Expr):
        pass


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


class AstPrinter(Visitor):
    def print(self, expr: Expr):
        return expr.accept(self)

    def visit_binary_expression(self, binary_expression: Expr):
        return self.parenthesize(
            binary_expression.operator.lexeme, binary_expression.left, binary_expression.right)

    def visit_grouping_expression(self, grouping_expression: Expr):
        return self.parenthesize('group', grouping_expression.expression)

    def visit_literal_expression(self, literal_expression: Expr):
        return literal_expression.value

    def visit_unary_expression(self, unary_expression: Expr):
        return self.parenthesize(unary_expression.operator.lexeme,
                                 unary_expression.right)

    def parenthesize(self, name: str, *exprs: Expr):
        string = ""
        for expr in exprs:
            string += str(expr.accept(self)) + " "
        return f"({name} {string})"


class Interpreter(Visitor):
    def evaluate(self, expr: Expr):
        return expr.accept(self)

    def visit_literal_expression(self, literal_expression: Expr) -> any:
        return literal_expression.value

    def visit_grouping_expression(self, grouping_expression: Expr) -> any:
        return self.evaluate(grouping_expression.expression)

    def visit_unary_expression(self, unary_expression: Expr) -> any:
        right = self.evaluate(unary_expression.right)

        if unary_expression.operator.type == tokens.MINUS:
            return -right
        elif unary_expression.operator.type == tokens.BANG:
            return not right

        return None

    def visit_binary_expression(self, binary_expression: Expr) -> any:
        left = self.evaluate(binary_expression.left)
        right = self.evaluate(binary_expression.right)

        if binary_expression.operator.type == tokens.MINUS:
            return left - right
        elif binary_expression.operator.type == tokens.SLASH:
            return left / right
        elif binary_expression.operator.type == tokens.STAR:
            return left * right
        elif binary_expression.operator.type == tokens.PLUS:
            if isinstance(left, str):
                return left + str(right)
            elif isinstance(right, str):
                return str(left) + right
            return left + right
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

        return None

