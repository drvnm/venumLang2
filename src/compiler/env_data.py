from typing import List
from parsing.statements import *
from intermediate.tokens import *

class DataHolder:
    def __init__(self, type: tokens, name: Token, expr: Expr, size: int):
        self.type = type
        self.name = name
        self.size = size

class StructData(DataHolder):
    def __init__(self, name: Token, members: List[DataHolder]):
        self.name = name
        self.members = members

class DataDeclr:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

class StructDeclr(DataDeclr):
    def __init__(self, name: str, size: int, members: List[DataDeclr]):
        super().__init__(name, size)
        self.members = members