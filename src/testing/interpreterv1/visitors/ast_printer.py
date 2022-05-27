from .visitor import Visitor
from parsing.expressions import *

class AstPrinter(Visitor):
    def print(self, expr: Expr):
        return expr.accept(self)

    def parenthesize(self, name: str, *exprs: Expr) -> None:
        string = ""
        
        for expr in exprs:
            string += f"{expr.accept(self)} "
            
        return f"({name} {string})"
    
    def visit_binary_expression(self, expr: BinaryExpr) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)
    
    def visit_literal_expression(self, expr: LiteralExpr) -> str:
        return expr.value.lexeme
    
    def visit_unary_expression(self, expr: UnaryExpr) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.right)
    
    def visit_grouping_expression(self, expr: GroupingExpr) -> str:
        return self.parenthesize("grouping", expr.expression)