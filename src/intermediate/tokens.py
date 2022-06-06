from dataclasses import dataclass
import enum

tokens = enum.Enum('tokens', """
        LEFT_PAREN RIGHT_PAREN LEFT_BRACE RIGHT_BRACE
        COMMA DOT MINUS PLUS SEMICOLON SLASH STAR AMPERSAND
        PLUS_EQUAL MINUS_EQUAL SLASH_EQUAL STAR_EQUAL PERCENT
        LEFT_SQUARE RIGHT_SQUARE LSHIFT RSHIFT LOGICAL_AND LOGICAL_OR

        BANG BANG_EQUAL
        EQUAL EQUAL_EQUAL
        GREATER GREATER_EQUAL
        LESS LESS_EQUAL

        IDENTIFIER STRING NUMBER

         CLASS ELSE FALSE FOR IF IN NULL OR
        PRINT RETURN SUPER THIS TRUE LET WHILE
        EXTERN
        ELIF CONTINUE BREAK FUNC SYSCALL STRUCT ASM
        IMPORT

        BYTE SHORT INT LONG BOOL STR CHAR VOID

        EOF
                    """)


@dataclass
class Token:
    type: tokens
    lexeme: str
    literal: any
    line: int
    col: int
    file: str = "NONE"
    line_content: str = ""
    

    def __repr__(self) -> str:
        return f'\n\tToken(type: {self.type}\n\tlexeme: {self.lexeme}\n\tliteral: {self.literal})\n\tline: {self.line}\n'
