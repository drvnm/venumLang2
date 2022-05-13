from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_binary_expression(self, binary_expression): ...

    @abstractmethod
    def visit_grouping_expression(self, grouping_expression): ...

    @abstractmethod
    def visit_literal_expression(self, literal_expression): ...

    @abstractmethod
    def visit_unary_expression(self, unary_expression): ...
