from .visitor import ExprVisitor
from parsing.expressions import *

# turns exprs like 3 + 3 into (+ 3 3)
class AstPrinter(ExprVisitor):
    def print(self, expr: Expr):
        return expr.accept(self)

    def visit_literal_expr(self, expr: LiteralExpr):
        return expr.value.lexeme if isinstance(expr.value, Token) else str(expr.value)

    def visit_binary_expr(self, expr: BinaryExpr):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_grouping_expr(self, expr: GroupingExpr):
        return self.parenthesize("group", expr.expression)
    
    def visit_unary_expr(self, expr: UnaryExpr):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name: str, *exprs: Expr):
        string = ""

        for expr in exprs:
            string += f"{expr.accept(self)} "

        return f"({name} {string})"
