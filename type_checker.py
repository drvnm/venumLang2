from typing import List
from tokens import tokens, Token
from process import error

addable_tokens = [tokens.INT, tokens.FLOAT]
integral_tokens = [tokens.PLUS, tokens.MIN, tokens.MUL, tokens.DIV, tokens.GT, tokens.GTE, tokens.LT, tokens.LTE, tokens.EQ]
readable_tokens = {
    tokens.INT: "int",
    tokens.FLOAT: "float",
    tokens.STRING: "string",
    tokens.PLUS: "+",
    tokens.MIN: "-",
    tokens.MUL: "*",
    tokens.DIV: "/",
    tokens.GT: ">",
    tokens.GTE: ">=",
    tokens.LT: "<",
    tokens.LTE: "<=",
    tokens.EQ: "==",
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
            elif token.type in integral_tokens:
                if len(stack) < 2:
                    error(f"Not enough operands for {readable_tokens[token.type]}", token.line, token.file, token.col)
                else:
                    right_operand = stack.pop()
                    left_operand = stack.pop()
                    if left_operand.type not in addable_tokens or right_operand.type not in addable_tokens:
                        error(f"Operands must be int or float, got {readable_tokens[left_operand.type]} and {readable_tokens[right_operand.type]}", token.line, token.file, token.col)
                    elif left_operand.type == tokens.FLOAT:
                        stack.append(Token(tokens.FLOAT, None, token.line, token.file, token.col))
                    else:
                        stack.append(Token(tokens.INT, None, token.line, token.file, token.col))
            # keywords
            elif token.type == tokens.PRINT:
                if len(stack) == 0:
                    error("Not enough operands for print", token.line, token.file, token.col)
                else:
                    continue
            elif token.type == tokens.PUTS:
                if len(stack) == 0:
                    error("Not enough operands for puts", token.line, token.file, token.col)
                else:
                    string = stack.pop()
                    if string.type != tokens.STRING:
                        error(f"puts expects str, got {readable_tokens[string.type]}", token.line, token.file, token.col)
            # branching, might improve this
            elif token.type == tokens.IFF:
                if len(stack) == 0:
                    error("Not enough operands for do", token.line, token.file, token.col)
                cond = stack.pop()
                if cond.type != tokens.INT:
                    error(f"if expects int, got {readable_tokens[cond.type]}", token.line, token.file, token.col)
            elif token.type == tokens.DO:
                continue
            elif token.type == tokens.ELSEF:
                continue
            elif token.type == tokens.END:
                continue