import sys
from tokens import *
from typing import List, Dict

# dict for determining how much bytes a type takes
type_size = {
    operations.INT: 8,
    operations.INT_8: 1,
    operations.INT_16: 2,
    operations.INT_32: 4,
    operations.INT_64: 8,
    operations.CHAR: 1,
}

# removes everything after // in src file


def remove_comments(lines: List[str]) -> List[str]:
    # remove comments
    new_lines = []

    for line in lines:
        line = line.split("//")[0]
        new_lines.append(line)

    # join lines
    return "\n".join(new_lines)


def error(msg: str, line: int, file_name: str, col: int) -> None:
    print(f"File: {file_name}, line: {line + 1}, col: {col}")
    print(f"   Error: {msg}")
    sys.exit(1)


class Lexer:
    def __init__(self, text: str, file_name: str):
        self.text: str = text
        self.pos: int = 0
        self.line: int = 0
        self.col: int = 0
        self.file_name: str = file_name
        self.operations: List[Operation] = []
        self.operators: str = "+-*/<>=!%&"
        self.function_names: Dict[str, Operation] = {}
        self.allowed_names: str = '_1234567890.[]'
        self.constants: Dict[str, str] = {}
        self.structs = {}
    # advances to the next character in the text

    def advance(self) -> None:
        if self.pos < len(self.text):
            self.pos += 1
            self.col += 1

    # methods for consuming literals
    def number(self) -> Operation:
        result = ""
        while self.pos < len(self.text) and (self.text[self.pos].isdigit() or self.text[self.pos] == "."):
            result += self.text[self.pos]
            self.advance()

        if result.count(".") > 1:
            error("Too many decimal points",
                  self.line, self.file_name, self.col)

        elif result[0] == "0" and len(result) > 1:
            error("Numbers cannot start with 0",
                  self.line, self.file_name, self.col)

        elif result.count(".") == 1:
            return Operation(operations.FLOAT_PUSH, float(result), self.line, self.file_name, self.col)
        else:
            return Operation(operations.INT_PUSH, int(result), self.line, self.file_name, self.col)

    def string(self) -> Operation:
        result = ""
        self.advance()
        while self.pos < len(self.text) and self.text[self.pos] != '"':
            result += self.text[self.pos]
            self.advance()
        self.advance()
        return Operation(operations.STRING_PUSH, result, self.line, self.file_name, self.col)

    def word(self) -> Operation:
        word = ""
        while self.pos < len(self.text) and (self.text[self.pos].isalpha() or self.text[self.pos] in self.allowed_names):
            word += self.text[self.pos]
            self.advance()
        if '[' in word and word[-1] == ']':
            arr_type = word.split('[')[0]
            if arr_type.upper() not in operations.__members__:
                error(f"Unknown type: {arr_type}",
                      self.line, self.file_name, self.col)
            arr_lenght = int(word.split('[')[1][:-1])

            byte_size = type_size[operations.__members__[
                arr_type.upper()]] * arr_lenght

            static_type = operations.__members__[arr_type.upper()]
            operation = Operation(static_type, arr_type,
                                  self.line, self.file_name, self.col)
            operations.static_type = static_type
            operation.size = byte_size
            operation.ISARR = True
            return operation
        if word.upper() in operations.__members__:
            return Operation(operations.__members__[word.upper()], word, self.line, self.file_name, self.col)
        elif word.upper() + "F" in operations.__members__:
            return Operation(operations.__members__[word.upper() + "F"], word, self.line, self.file_name, self.col)
        else:
            return Operation(operations.IDENTIFIER, word, self.line, self.file_name, self.col)

    def operator(self) -> Operation:
        operator = ""
        while self.pos < len(self.text) and self.text[self.pos] in self.operators:
            operator += self.text[self.pos]
            self.advance()
        return Operation(operator_table[operator], operator, self.line, self.file_name, self.col)

    def lex(self):
        while self.pos < len(self.text):
            if self.text[self.pos] == " ":
                self.advance()

            elif self.text[self.pos] == "\n":
                self.line += 1
                self.advance()
                self.col = 0

            # literal characters
            elif self.text[self.pos].isdigit():
                self.operations.append(self.number())
            elif self.text[self.pos] == '"':
                self.operations.append(self.string())

            # keywords
            elif self.text[self.pos].isalpha():
                self.operations.append(self.word())

            # operators
            elif self.text[self.pos] in self.operators:
                self.operations.append(self.operator())
            else:
                error("Unknown character", self.line, self.file_name, self.col)

    # helper methods
    def print_program(self) -> None:
        print(f"stack length: {len(self.operations)}")
        for Operation in self.operations:
            if hasattr(Operation, "size"):
                print(f"{Operation} | at {Operation.size}")
            elif Operation.type == operations.FUNC:
                print(f"{Operation} | takes {Operation.num_args} args")
            else:
                print(Operation)

    def generate_blocks(self) -> None:
        stack = []
        # loop that cross references blocks like while or if statements.
        for index in range(len(self.operations)):
            curr_in = self.operations[index]
            if curr_in.type == operations.IFF:
                stack.append(index)
            elif curr_in.type == operations.ELSEF:
                if_index = stack.pop()
                self.operations[if_index].jump = index + 1
                stack.append(index)
            elif curr_in.type == operations.END:
                block_ip = stack.pop()
                if self.operations[block_ip].type == operations.IFF or self.operations[block_ip].type == operations.ELSEF:
                    self.operations[block_ip].jump = index + 1
                else:
                    self.operations[block_ip].jump = index + 1
                    self.operations[index].jump = self.operations[block_ip].while_ip
            elif curr_in.type == operations.CONTINUEF:
                do_ip = stack.pop()
                self.operations[index].jump = self.operations[do_ip].while_ip
                stack.append(do_ip)
            elif curr_in.type == operations.WHILEF:
                stack.append(index)
            elif curr_in.type == operations.DO:
                while_ip = stack.pop()
                self.operations[index].while_ip = while_ip
                stack.append(index)

    # replaces the constants in the program
    def replace_constant(self, index: int, value: any, curr_op: Operation):
        # check if value is string or integer
        if isinstance(value, str):
            self.operations[index] = Operation(
                operations.STRING_PUSH, value, curr_op.line, curr_op.file, curr_op.col)
        else:
            self.operations[index] = Operation(
                operations.INT_PUSH, value, curr_op.line, curr_op.file, curr_op.col)

    def generate_variables(self) -> None:
        names = {}
        index = 0
        memory_index = 0  # keeps track of where new memory begins
        stack = []

        while index < len(self.operations):
            current_Operation = self.operations[index]
            if current_Operation.type == operations.VAR:
                identifier = self.operations[index + 1]
                type_Operation = self.operations[index + 2]

                # check if the name already exists
                if identifier.value in names:
                    error(f"Variable {identifier.value} already exists",
                          current_Operation.line, self.file_name, current_Operation.col)
                del self.operations[index + 1: index + 3]
                operation = Operation(operations.VARIABLE, identifier.value,
                                      current_Operation.line, self.file_name, current_Operation.col)
                operation.static_type = type_Operation.type
                operation.size = memory_index
                print(type_Operation.type)
                memory_index += type_size[type_Operation.type] if not hasattr(type_Operation, 'ISARR') else type_Operation.size
                self.operations[index] = operation
                names[identifier.value] = operation
                index += 1
            elif current_Operation.type == operations.IDENTIFIER:
                # handle variable
                if current_Operation.value in names:
                    self.operations[index].size = names[current_Operation.value].size
                    self.operations[index].static_type = names[current_Operation.value].static_type
                    index += 1
                # handle function calls
                elif current_Operation.value in self.function_names:
                    self.operations[index] = Operation(
                        operations.FUNC_CALL, current_Operation.value, current_Operation.line, current_Operation.file, current_Operation.col)
                    index += 1
                # handle constant replace
                elif current_Operation.value in self.constants:
                    self.replace_constant(
                        index, self.constants[current_Operation.value], current_Operation)
                    index += 1
                elif '.' in current_Operation.value:

                    struct_name, idx = current_Operation.value.split('.')
                    print(idx)
                    struct_info = self.structs[struct_name][int(idx)]
                    print(struct_info)
                    self.operations[index].static_type = struct_info[0]
                    self.operations[index].size = struct_info[1]
                    index += 1

                else:
                    error(f"Variable {current_Operation.value} not found",
                          current_Operation.line, self.file_name, current_Operation.col)

            elif current_Operation.type == operations.FUNC:
                current_Operation.num_args = 0
                current_Operation.arg_types = []
                function_name = self.operations[index + 1]
                self.function_names[function_name.value] = self.operations[index]
                function_name.type = operations.FUNC_NAME
                current_Operation.name = function_name.value
                stack.append(index)
                index += 1
                while self.operations[index].type != operations.IN:
                    if self.operations[index].type in matching_operations:
                        function_index = stack.pop()
                        self.operations[function_index].num_args += 1
                        self.operations[function_index].arg_types.append(
                            self.operations[index].type)
                        stack.append(function_index)
                    index += 1
            elif current_Operation.type == operations.END:
                function_index = stack.pop()
                if self.operations[function_index].type == operations.FUNC:
                    self.operations[index].type = operations.FUNC_END
                index += 1
            elif current_Operation.type == operations.IFF:
                stack.append(index)
                index += 1
            elif current_Operation.type == operations.DO:
                stack.append(index)
                index += 1
            elif current_Operation.type == operations.CONST:
                const_name = self.operations[index + 1]
                const_value = self.operations[index + 2]
                if const_name.value in names or const_name.value in self.constants or const_name.value in self.function_names:
                    error(f"Constant {const_name.value} already exists",
                          current_Operation.line, self.file_name, current_Operation.col)
                del self.operations[index: index + 3]
                self.constants[const_name.value] = const_value.value
            elif current_Operation.type == operations.STRUCT:
                struct_name = self.operations[index + 1]
                self.structs[struct_name.value] = []
                last_index = index
                index += 2
                while self.operations[index].type != operations.END:
                    field_size = type_size[self.operations[index].type]
                    self.structs[struct_name.value].append(
                        [
                            self.operations[index].type,
                            memory_index
                        ]
                    )
                    memory_index += field_size
                    index += 1
                index += 1
              
                del self.operations[last_index: index]
                index -= (index - last_index)
            else:
                index += 1
