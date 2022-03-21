from typing import List
from tokens import tokens, Token
from process import error

addable_tokens = [tokens.INT, tokens.FLOAT]
readable_tokens = {
    tokens.INT: "int",
    tokens.FLOAT: "float",
    tokens.STRING: "string",
    tokens.PLUS: "+",
}

class TypeChecker:
    def __init__(self, tokens: List[Token]): 
        self.tokens = tokens
    
    def check(self) -> None:
        stack = []
        for token in self.tokens:
            if token.type == tokens.INT or token.type == tokens.FLOAT:
                stack.append(token)
            elif token.type == tokens.STRING:
                stack.append(token)
            elif token.type == tokens.PLUS:
                if len(stack) < 2:
                    error("Not enough operands for +", token.line, token.file, token.col)
                else:
                    left_operand = stack.pop()
                    right_operand = stack.pop()
                    if left_operand.type not in addable_tokens or right_operand.type not in addable_tokens:
                        error(f"Operands must be int or float, got {readable_tokens[left_operand.type]} and {readable_tokens[right_operand.type]}", token.line, token.file, token.col)