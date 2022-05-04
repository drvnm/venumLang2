from .visitor import Visitor
from parsing.expressions import *


class RpnPrinter(Visitor):
    def print(self, expr: Expr):
        return expr.accept(self)
    
    def rpn_ify(self, name: str, *exprs: Expr):
        string = ""
        
        for expr in exprs:
            string += f"{expr.accept(self)} "
        
        return f"{string} {name}"
            
        
    def visit_binary_expression(self, expr: BinaryExpr) -> str:
        return self.rpn_ify(expr.operator.lexeme, expr.left, expr.right)

    def visit_literal_expression(self, expr: LiteralExpr) -> str:
        return expr.value.lexeme
    
    def visit_unary_expression(self, expr: UnaryExpr) -> str:
        pass
    
    def visit_grouping_expression(self, grouping_expression: Expr):
        pass