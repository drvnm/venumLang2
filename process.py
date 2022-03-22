import sys
from tokens import tokens, Token, operator_table
from typing import List

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
        self.operators: List[str] = ["+", "-", "*", "/", "<", ">", "="]
    
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
            error("Too many decimal points", self.line, self.file_name, self.col)
        
        elif result[0] == "0" and len(result) > 1:
            error("Numbers cannot start with 0", self.line, self.file_name, self.col)
        
        elif result.count(".") == 1:
            return Token(tokens.FLOAT, float(result), self.line, self.file_name, self.col)
        else:
            return Token(tokens.INT, int(result), self.line, self.file_name, self.col)
    
    def string(self) -> Token:
        result = ""
        self.advance()
        while self.pos < len(self.text) and self.text[self.pos] != '"':
            result += self.text[self.pos]
            self.advance()
        self.advance()
        return Token(tokens.STRING, result, self.line, self.file_name, self.col)
    
    def word(self) -> Token:
        word = ""
        while self.pos < len(self.text) and self.text[self.pos].isalpha():
            word += self.text[self.pos]
            self.advance()
        if word.upper() in tokens.__members__:
            return Token(tokens.__members__[word.upper()], word, self.line, self.file_name, self.col)
        else:
            error("Unknown keyword", self.line, self.file_name, self.col)
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
                error("Unknown character at", self.line, self.file_name, self.col)
    
    # helper methods
    def print_tokens(self) -> None:
        for token in self.tokens:
            print(token)