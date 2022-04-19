from preprocessing.operations import *
from preprocessing.lookup_tables import *
from preprocessing.helper_functions import *
from typing import List, Dict
import os


class Lexer:
    def __init__(self, text: str, file_name: str):
        self.text: str = text
        self.pos: int = 0
        self.line: int = 0
        self.col: int = 0
        self.file_name: str = file_name
        self.operations: List[Operation] = []
        self.operators: str = "+-*/#<>=!%&"
        self.function_names: Dict[str, Operation] = {}
        self.allowed_names: str = '_123456#!789*0.[]()'

        # attributes of the program
        self.constants: Dict[str, str] = {}
        self.structs = {}
        self.variables = {}
        self.memory_index = 0
        self.line_content: str = ""

    # advances to the next character in the text

    def advance(self) -> None:
        if self.pos < len(self.text):
            self.line_content += self.text[self.pos]
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
                  self.line, self.file_name, self.col, self.line_content)

        elif result[0] == "0" and len(result) > 1:
            error("Numbers cannot start with 0",
                  self.line, self.file_name, self.col, self.line_content)

        elif result.count(".") == 1:
            return Operation(operations.FLOAT_PUSH, float(result), self.line, self.file_name, self.col, self.line_content)
        else:
            return Operation(operations.INT_PUSH, int(result), self.line, self.file_name, self.col, self.line_content)

    def string(self) -> Operation:
        result = ""
        self.advance()
        while self.pos < len(self.text) and self.text[self.pos] != '"':
            result += self.text[self.pos]
            self.advance()
        self.advance()
        return Operation(operations.STRING_PUSH, result, self.line, self.file_name, self.col, self.line_content)

    def word(self) -> Operation:
        ops = operations.__members__
        word = ""
        while self.pos < len(self.text) and (self.text[self.pos].isalpha() or self.text[self.pos] in self.allowed_names):
            word += self.text[self.pos]
            self.advance()

        # if a [] is found, word is probably an array
        if '[' in word and word[-1] == ']':
            arr_type = word.split('[')[0]
            if arr_type.upper() not in ops:
                error(f"Unknown type: {arr_type}",
                      self.line, self.file_name, self.col, self.line_content)
            arr_lenght = int(word.split('[')[1][:-1])

            byte_size = type_size[ops[
                arr_type.upper()]] * arr_lenght

            static_type = ops[arr_type.upper()]
            operation = Operation(static_type, arr_type,
                                  self.line, self.file_name, self.col, self.line_content)
            operations.static_type = static_type
            operation.size = byte_size
            operation.ISARR = True
            return operation

        # check if last char is *, means word is a dereference, replace with identifier and load
        if word[-1] == '*':
            word = word[:-1]
            self.operations.append(Operation(operations.IDENTIFIER, word, self.line,
                                             self.file_name, self.col, self.line_content))
            return Operation(operations.LOAD, "load", self.line,
                             self.file_name, self.col, self.line_content)

        # if last char is !, use write operation
        if word[-1] == '!':
            word = word[:-1]
            self.operations.append(Operation(operations.IDENTIFIER, word, self.line,
                                             self.file_name, self.col, self.line_content))
            return Operation(operations.WRITE, "write", self.line,
                             self.file_name, self.col, self.line_content)

        # parsing types
        elif word in builtin_types:
            operation = Operation(
                ops[word.upper()], word, self.line, self.file_name, self.col, self.line_content)
            operation.size = type_size[ops[word.upper()]]
            return operation

        if word.upper() in ops:
            return Operation(ops[word.upper()], word, self.line, self.file_name, self.col, self.line_content)
        else:
            return Operation(operations.IDENTIFIER, word, self.line, self.file_name, self.col, self.line_content)

    def operator(self) -> Operation:
        operator = ""
        while self.pos < len(self.text) and self.text[self.pos] in self.operators:
            operator += self.text[self.pos]
            self.advance()
        return Operation(operator_table[operator], operator, self.line, self.file_name, self.col, self.line_content)

    def lex(self):
        while self.pos < len(self.text):
            if self.text[self.pos] == " ":
                self.advance()

            # when \n is encountered, reset the column and increment the line
            elif self.text[self.pos] == "\n":
                self.line += 1
                self.advance()
                self.col = 0
                self.line_content = ""

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
                error("Unknown character", self.line,
                      self.file_name, self.col, self.line_content)

    # helper methods
    def print_program(self) -> None:
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
            if curr_in.type == operations.IF:
                stack.append(index)
            elif curr_in.type == operations.ELSE:
                if_index = stack.pop()
                self.operations[if_index].jump = index + 1
                stack.append(index)
            elif curr_in.type == operations.END:
                block_ip = stack.pop()
                if self.operations[block_ip].type == operations.IF or self.operations[block_ip].type == operations.ELSE:
                    self.operations[block_ip].jump = index + 1
                else:
                    self.operations[block_ip].jump = index + 1
                    self.operations[index].jump = self.operations[block_ip].while_ip
            elif curr_in.type == operations.CONTINUEF:
                do_ip = stack.pop()
                self.operations[index].jump = self.operations[do_ip].while_ip
                stack.append(do_ip)
            elif curr_in.type == operations.WHILE:
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
                operations.STRING_PUSH, value, curr_op.line, curr_op.file, curr_op.col, curr_op.line_content)
        else:
            self.operations[index] = Operation(
                operations.INT_PUSH, value, curr_op.line, curr_op.file, curr_op.col, curr_op.line_content)

    def generate_symbols(self) -> None:
        from preprocessing.generate_tokens import generate_tokens

        self.variables = {}
        index = 0
        self.memory_index = 0  # keeps track of where new memory begins
        stack = []

        while index < len(self.operations):
            current_Operation = self.operations[index]
            if current_Operation.type == operations.VAR:
                identifier = self.operations[index + 1]
                type_Operation = self.operations[index + 2]

                # check if the name already exists
                if identifier.value in self.variables:
                    error(f"Symbol {identifier.value} already exists",
                          current_Operation.line, self.file_name, current_Operation.col, current_Operation.line_content)
                del self.operations[index + 1: index + 3]
                operation = Operation(operations.VARIABLE, identifier.value,
                                      current_Operation.line, self.file_name, current_Operation.col, current_Operation.line_content)
                operation.static_type = type_Operation.type
                operation.size = self.memory_index
                self.memory_index += type_size[type_Operation.type] if not hasattr(
                    type_Operation, 'ISARR') else type_Operation.size
                self.operations[index] = operation
                self.variables[identifier.value] = operation
                index += 1

            elif current_Operation.type == operations.IDENTIFIER:
                # handle variable
                if current_Operation.value in self.variables:
                    self.operations[index].size = self.variables[current_Operation.value].size
                    self.operations[index].static_type = self.variables[current_Operation.value].static_type
                    index += 1
                # handle function calls
                elif current_Operation.value in self.function_names:
                    self.operations[index] = Operation(
                        operations.FUNC_CALL, current_Operation.value, current_Operation.line, current_Operation.file, current_Operation.col, current_Operation.line_content)
                    index += 1
                # handle constant replace
                elif current_Operation.value in self.constants:
                    self.replace_constant(
                        index, self.constants[current_Operation.value], current_Operation)
                    index += 1
                elif '.' in current_Operation.value:

                    struct_name, idx = current_Operation.value.split('.')
                    struct_info = self.structs[struct_name][int(idx)]
                    self.operations[index].static_type = struct_info[0]
                    self.operations[index].size = struct_info[1]
                    index += 1

                else:
                    error(f"Symbol {current_Operation.value} not found",
                          current_Operation.line, self.file_name, current_Operation.col, current_Operation.line_content)

            elif current_Operation.type == operations.FUNC:
                current_Operation.num_args = 0
                current_Operation.arg_types = []
                function_name = self.operations[index + 1]  # function name
                # if function_name.value in self.function_names:
                #     error(f"Function {function_name.value} already exists",
                #           current_Operation.line, self.file_name, current_Operation.col)
                self.function_names[function_name.value] = self.operations[index]
                function_name.type = operations.FUNC_NAME
                current_Operation.name = function_name.value
                stack.append(index)
                index += 1
                # loop through arguments, we need this later to pop into correct registers
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
            elif current_Operation.type == operations.IF:
                stack.append(index)
                index += 1
            elif current_Operation.type == operations.DO:
                stack.append(index)
                index += 1
            elif current_Operation.type == operations.CONST:
                const_name = self.operations[index + 1]
                const_value = self.operations[index + 2]
                if const_name.value in self.variables or const_name.value in self.constants or const_name.value in self.function_names:
                    error(f"Constant {const_name.value} already exists",
                          current_Operation.line, self.file_name, current_Operation.col, current_Operation.line_content)
                del self.operations[index: index + 3]
                self.constants[const_name.value] = const_value.value
            elif current_Operation.type == operations.STRUCT:
                struct_name = self.operations[index + 1]
                self.structs[struct_name.value] = []
                last_index = index
                index += 2
                while self.operations[index].type != operations.END:
                    print(self.operations[index].type)
                    field_size = self.operations[index].size
                    self.structs[struct_name.value].append(
                        [
                            self.operations[index].type,
                            self.memory_index
                        ]
                    )
                    self.memory_index += field_size
                    index += 1
                index += 1

                del self.operations[last_index: index]
                index -= (index - last_index)
            elif current_Operation.type == operations.INCLUDE:
                file_name = self.operations[index + 1].value
                if not os.path.isfile(file_name):  # check if the file exists
                    error(f"File {file_name} not found",
                          current_Operation.line, self.file_name, current_Operation.col, current_Operation.line_content)
                # delete the include operation
                del self.operations[index: index + 2]
                # all the info that is needed from the different file
                other_ops, function_names, variables, memory, constants = generate_tokens(
                    file_name
                )
                self.operations[index: index] = other_ops
                self.function_names = {
                    **self.function_names,
                    **function_names
                }
                self.variables = {
                    **self.variables,
                    **variables
                }
                self.constants = {
                    **self.constants,
                    **constants
                }
                self.memory_index += memory
            else:
                index += 1
