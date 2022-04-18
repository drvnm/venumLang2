from typing import List
from preprocessing.operations import operations, Operation
from preprocessing.process import error

addable_operations = [operations.INT_PUSH, operations.FLOAT_PUSH]
integral_operations = [operations.PLUS, operations.MIN, operations.MUL, operations.DIV, operations.GT, operations.GTE, operations.LT, operations.LTE, operations.EQ]
readable_operations = {
    operations.INT_PUSH: "int",
    operations.FLOAT_PUSH: "float",
    operations.STRING_PUSH: "string",
    operations.PLUS: "+",
    operations.MIN: "-",
    operations.MUL: "*",
    operations.DIV: "/",
    operations.GT: ">",
    operations.GTE: ">=",
    operations.LT: "<",
    operations.LTE: "<=",
    operations.EQ: "==",
}

class TypeChecker:
    def __init__(self, operations: List[Operation]): 
        self.operations = operations
    
    def check(self) -> None:
        stack = []
        for token in self.operations:
            if token.type == operations.INT_PUSH or token.type == operations.FLOAT_PUSH:
                stack.append(token)
            elif token.type == operations.STRING_PUSH:
                stack.append(token)
            elif token.type in integral_operations:
                if len(stack) < 2:
                    error(f"Not enough operands for {readable_operations[token.type]}", token.line, token.file, token.col)
                else:
                    right_operand = stack.pop()
                    left_operand = stack.pop()
                    if left_operand.type not in addable_operations or right_operand.type not in addable_operations:
                        error(f"Operands must be int or float, got {readable_operations[left_operand.type]} and {readable_operations[right_operand.type]}", token.line, token.file, token.col)
                    elif left_operand.type == operations.FLOAT_PUSH:
                        stack.append(Operation(operations.FLOAT_PUSH, None, token.line, token.file, token.col))
                    else:
                        stack.append(Operation(operations.INT_PUSH, None, token.line, token.file, token.col))
            # keywords
            elif token.type == operations.PRINT:
                if len(stack) == 0:
                    error("Not enough operands for print", token.line, token.file, token.col)
                else:
                    continue
            elif token.type == operations.PUTS:
                if len(stack) == 0:
                    error("Not enough operands for puts", token.line, token.file, token.col)
                else:
                    string = stack.pop()
                    if string.type != operations.STRING_PUSH:
                        error(f"puts expects str, got {readable_operations[string.type]}", token.line, token.file, token.col)
            # branching, might improve this
            elif token.type == operations.IFF:
                if len(stack) == 0:
                    error("Not enough operands for do", token.line, token.file, token.col)
                cond = stack.pop()
                if cond.type != operations.INT_PUSH:
                    error(f"if expects int, got {readable_operations[cond.type]}", token.line, token.file, token.col)
            elif token.type == operations.DO:
                continue
            elif token.type == operations.ELSEF:
                continue
            elif token.type == operations.END:
                continue