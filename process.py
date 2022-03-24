import sys
from tokens import *
from typing import List

# dict for determining how much bytes a type takes
type_size = {
    tokens.INT: 8,
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
        self.tokens: List[Token] = []
        self.operators: List[str] = [
            "+", "-", "*", "/", "<", ">", "=", "!", "%"]

    # advances to the next character in the text
    def advance(self) -> None:
        if self.pos < len(self.text):
            self.pos += 1
            self.col += 1

    # methods for consuming literals
    def number(self) -> Token:
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
            return Token(tokens.FLOAT_PUSH, float(result), self.line, self.file_name, self.col)
        else:
            return Token(tokens.INT_PUSH, int(result), self.line, self.file_name, self.col)

    def string(self) -> Token:
        result = ""
        self.advance()
        while self.pos < len(self.text) and self.text[self.pos] != '"':
            result += self.text[self.pos]
            self.advance()
        self.advance()
        return Token(tokens.STRING_PUSH, result, self.line, self.file_name, self.col)

    def word(self) -> Token:
        word = ""
        while self.pos < len(self.text) and self.text[self.pos].isalpha():
            word += self.text[self.pos]
            self.advance()
        if word.upper() in tokens.__members__:
            return Token(tokens.__members__[word.upper()], word, self.line, self.file_name, self.col)
        elif word.upper() + "F" in tokens.__members__:
            return Token(tokens.__members__[word.upper() + "F"], word, self.line, self.file_name, self.col)
        else:
            return Token(tokens.IDENTIFIER, word, self.line, self.file_name, self.col)

    def operator(self) -> Token:
        operator = ""
        while self.pos < len(self.text) and self.text[self.pos] in self.operators:
            operator += self.text[self.pos]
            self.advance()
        return Token(operator_table[operator], operator, self.line, self.file_name, self.col)

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
                self.tokens.append(self.number())
            elif self.text[self.pos] == '"':
                self.tokens.append(self.string())

            # keywords
            elif self.text[self.pos].isalpha():
                self.tokens.append(self.word())

            # operators
            elif self.text[self.pos] in self.operators:
                self.tokens.append(self.operator())
            else:
                error("Unknown character", self.line, self.file_name, self.col)

    # helper methods
    def print_tokens(self) -> None:
        print(f"stack length: {len(self.tokens)}")
        for token in self.tokens:
            if hasattr(token, "size"):
                print(f"{token} | at {token.size}")
            else:
                print(token)

    def generate_blocks(self) -> None:
        stack = []
        for index in range(len(self.tokens)):
            curr_in = self.tokens[index]
            if curr_in.type == tokens.IFF:
                stack.append(index)
            elif curr_in.type == tokens.ELSEF:
                if_index = stack.pop()
                self.tokens[if_index].jump = index + 1
                stack.append(index)
            elif curr_in.type == tokens.END:
                block_ip = stack.pop()
                if self.tokens[block_ip].type == tokens.IFF or self.tokens[block_ip].type == tokens.ELSEF:
                    self.tokens[block_ip].jump = index + 1
                else:
                    self.tokens[block_ip].jump = index + 1
                    self.tokens[index].jump = self.tokens[block_ip].while_ip
            elif curr_in.type == tokens.WHILEF:
                stack.append(index)
            elif curr_in.type == tokens.DO:
                while_ip = stack.pop()
                self.tokens[index].while_ip = while_ip
                stack.append(index)

    def generate_variables(self) -> None:
        names = {}
        index = 0
        memory_index = 0
        stack = []
        function_names = {}

        while index < len(self.tokens):
            current_token = self.tokens[index]
            if current_token.type == tokens.VAR:
                identifier = self.tokens[index + 1]
                type_token = self.tokens[index + 2]

                # check if the name already exists
                if identifier.value in names:
                    error(f"Variable {identifier.value} already exists",
                          current_token.line, self.file_name, current_token.col)
                del self.tokens[index + 1: index + 3]
                token = Token(tokens.VARIABLE, identifier.value,
                              current_token.line, self.file_name, current_token.col)
                token.static_type = type_token.type
                token.size = memory_index
                memory_index += type_size[type_token.type]
                self.tokens[index] = token
                names[identifier.value] = token
                index += 1
            elif current_token.type == tokens.IDENTIFIER:
                if current_token.value in names:
                    self.tokens[index].size = names[current_token.value].size
                    index += 1
                elif current_token.value in function_names:
                    self.tokens[index] = Token(tokens.FUNC_CALL, current_token.value, current_token.line, current_token.file, current_token.col)
                
                else:
                    error(f"Variable {current_token.value} not found",
                          current_token.line, self.file_name, current_token.col)

            elif current_token.type == tokens.FUNC:
                function_name = self.tokens[index + 1]
                function_names[function_name.value] = index
                function_name.type = tokens.FUNC_NAME
                current_token.name = function_name.value
                stack.append(index)
                index += 1

            elif current_token.type == tokens.END:
                function_index = stack.pop()
                if self.tokens[function_index].type == tokens.FUNC:
                    self.tokens[index].type = tokens.FUNC_END
                index += 1
            elif current_token.type == tokens.IFF:
                stack.append(index)
                index += 1
            elif current_token.type == tokens.DO:
                stack.append(index)
                index += 1

            else:
                index += 1
