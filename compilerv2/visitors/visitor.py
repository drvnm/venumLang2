from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_literal_expr(self, literal_expression): ...

    @abstractmethod
    def visit_grouping_expr(self, grouping_expression): ...

    @abstractmethod
    def visit_unary_expr(self, unary_expression): ...

    @abstractmethod
    def visit_binary_expr(self, binary_expression): ...
