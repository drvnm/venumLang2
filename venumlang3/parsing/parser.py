from typing import List
from intermediate.tokens import *
from .expressions import *

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
    
    def expression(self) -> Expr:
        return self.equality()