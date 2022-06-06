from typing import List
from venumlang.intermediate.tokens import *
from venumlang.intermediate.lookup_tables import *
from .error import *

# class that peforms lexical analysis


class Lexer:
    def __init__(self, source: str, file: str):
        self.file = file
        self.source = source
        self.tokens: List[Token] = []

        # data used for creating new tokens
        self.start = 0
        self.current = 0
        self.line = 1
        self.col = 0
        self.line_content = ""

        self.whitespace = [' ', '\t', '\n', '\r']
        self.allowed_hex = "0123456789abcdefABCDEF"

    def at_end(self) -> bool:  # check if at end of source code
        return self.current >= len(self.source)

    def is_whitespace(self) -> bool:  # check if current char is whitespace
        return self.source[self.current] in self.whitespace

    def advance(self) -> None:  # advance current char
        if not self.at_end():
            self.line_content += self.get_current_char()
            self.current += 1
            self.col += 1

    def get_current_char(self) -> str:  # get current char
        return self.source[self.current]

    def add_token(self, token_type: tokens, lexeme, literal=None) -> None:
        self.tokens.append(
            Token(token_type, lexeme, literal, self.line, self.col, self.file, self.line_content))

    def peek_next_char(self) -> str:  # get next char
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current + 1]

    # methods that hangle literals
    def string(self) -> None:
        string = ''
        self.advance()
        while not self.at_end() and self.get_current_char() != '"':
            if self.get_current_char() == '\n':
                self.line += 1
                self.advance()
            else:
                string += self.get_current_char()
                self.advance()

        if self.at_end():
            error(self.line, 'Unterminated string')
        else:
            self.advance()
            self.add_token(tokens.STRING, string, str(string))
    
    def hex_number(self, number: str) -> None:
        self.advance()  # skip x
        if self.at_end() or self.get_current_char() not in self.allowed_hex:
            error(self.line, 'Unterminated hex number')
        while not self.at_end() and (self.get_current_char().isdigit() or self.get_current_char() in self.allowed_hex):
            number += self.get_current_char()
            self.advance()

        self.add_token(tokens.NUMBER, number, int(number, 16))
    
    def binary_number(self, number: str) -> None:
        self.advance()  # skip b
        if self.at_end() or self.get_current_char() not in "01":
            error(self.line, 'Unterminated binary number')
        while not self.at_end() and self.get_current_char().isdigit():
            number += self.get_current_char()
            self.advance()

        self.add_token(tokens.NUMBER, number, int(number, 2))

    def number(self) -> None:
        number = ''
        number += self.get_current_char()
        self.advance() # skip first decimal
        if not self.at_end():
            char = self.get_current_char()
            if char == 'x':
                number += char
                self.hex_number(number)
                return
            elif char == 'b':
                number += char
                self.binary_number(number)
                return
        
        while not self.at_end() and self.get_current_char().isdigit():
            number += self.get_current_char()
            self.advance()

        if not self.at_end() and self.get_current_char() == '.':
            number += self.get_current_char()
            self.advance()

            while not self.at_end() and self.get_current_char().isdigit():
                number += self.get_current_char()
                self.advance()

            self.add_token(tokens.NUMBER, number, float(number))
        else:
            self.add_token(tokens.NUMBER, number, int(number))

    def char(self) -> None:
        self.advance()  # skip '
        char = self.get_current_char()
        self.advance()  # skip char
        if char == '\\':
            char += self.get_current_char()
            char = char.encode().decode('unicode_escape')
            self.advance()
        if self.get_current_char() != "'":
            error(self.tokens[-1], 'Unterminated char')
        else:
            self.advance()
            self.add_token(tokens.CHAR, char, char)

    def identifier(self) -> None:
        identifier = ''
        while not self.at_end() and (char := self.get_current_char()).isalnum() or char == '_':
            identifier += char
            self.advance()

        if identifier in word_to_keyword:
            self.add_token(word_to_keyword[identifier], identifier)
        else:
            self.add_token(tokens.IDENTIFIER, identifier)

    def scan(self) -> None:
        while not self.at_end():
            while not self.at_end() and self.is_whitespace():
                if self.get_current_char() == '\n':
                    self.col = 0
                    self.line += 1
                    self.line_content = ""
                self.advance()

            if self.at_end():
                self.add_token(tokens.EOF, None)
                return

            char = self.get_current_char()
            # handle / for comments and divide
            if char == '/':
                if self.peek_next_char() == '/':
                    while not self.at_end() and self.get_current_char() != '\n':
                        self.advance()
                else:
                    self.add_token(tokens.SLASH, char)
                    self.advance()

            # handle single char tokens, like + ( ) { }
            elif char in single_char_tokens:
                if self.peek_next_char() == '=':
                    self.add_token(
                        optional_to_token[char + self.peek_next_char()], char + self.peek_next_char())
                    self.advance()
                    self.advance()
                else:
                    token = single_char_tokens[char]
                    self.add_token(token, char)
                    self.advance()

            # handle 2 char tokens like == and !=
            elif char in two_char_tokens:
                if (second_char := self.peek_next_char()) == two_char_tokens[char]:
                    token = optional_to_token[char + second_char]
                    self.add_token(token, char + second_char)
                    self.advance()
                    self.advance()
                else:
                    token = optional_to_token[char]
                    self.add_token(token, char)
                    self.advance()

            elif char == '"':
                self.string()

            elif char == "'":
                self.char()

            elif char.isdigit():
                self.number()

            elif char.isalnum() or char == '_':
                self.identifier()

            else:
                error(
                    Token(
                        tokens.SEMICOLON, None,
                        None, self.line, self.col, self.file, self.line_content
                        ), f'Unexpected character {self.get_current_char()}'
                )

            if self.at_end():
                self.add_token(tokens.EOF, None)
                return
