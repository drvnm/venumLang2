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
        return literal_expression.value.lexeme

    def visit_unary_expression(self, unary_expression: Expr):
        return self.parenthesize(unary_expression.operator.lexeme,
                          unary_expression.right)

    def parenthesize(self, name: str, *exprs: Expr):
        string = ""
        for expr in exprs:
            string += expr.accept(self) + " "
        return f"({name} {string})"



expression = BinaryExpr(
    UnaryExpr(
        Token(tokens.MINUS, '-', None, 1),
        LiteralExpr(Token(tokens.NUMBER, '123', None, 1))
    ),
    Token(tokens.STAR, '*', None, 1),
    GroupingExpr(
        LiteralExpr(Token(tokens.NUMBER, '45.67', None, 1))
    )
)

print(AstPrinter().print(expression))
