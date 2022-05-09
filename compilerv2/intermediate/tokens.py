from dataclasses import dataclass
import enum

tokens = enum.Enum('tokens', """
        LEFT_PAREN RIGHT_PAREN LEFT_BRACE RIGHT_BRACE
        COMMA DOT MINUS PLUS SEMICOLON SLASH STAR

        BANG BANG_EQUAL
        EQUAL EQUAL_EQUAL
        GREATER GREATER_EQUAL
        LESS LESS_EQUAL

        IDENTIFIER STRING NUMBER

        AND CLASS ELSE FALSE FOR IF IN NULL OR
        PRINT RETURN SUPER THIS TRUE LET WHILE

        BYTE SHORT INT LONG BOOL

        EOF
                    """)


@dataclass
class Token:
    type: tokens
    lexeme: str
    literal: any
    line: int

    def __repr__(self) -> str:
        return f'\n\tToken(type: {self.type}\n\tlexeme: {self.lexeme}\n\tliteral: {self.literal})\n\tline: {self.line}\n'
