from abc import ABC, abstractmethod

class ExprVisitor(ABC):
    @abstractmethod
    def visit_literal_expr(self, literal_expression): ...

    @abstractmethod
    def visit_grouping_expr(self, grouping_expression): ...

    @abstractmethod
    def visit_unary_expr(self, unary_expression): ...

    @abstractmethod
    def visit_binary_expr(self, binary_expression): ...

class StmtVisitor(ABC):
    @abstractmethod
    def visit_print_stmt(self, print_stmt): ...

    @abstractmethod
    def visit_expr_stmt(self, expr_stmt): ...