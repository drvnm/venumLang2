from enum import Enum

tokens = Enum('tokens', """ 

            LITERALS
            INT
            FLOAT
            STRING

            OPERATORS
            PLUS

            KEYWORDS
            PRINT
                        """)

class Token:
    def __init__(self, type_: tokens, 
                value: any, 
                line: int, 
                file_name: str,
                col: int
                ) -> None:

        self.type: tokens = type_
        self.value: any = value
        self.line: int = line
        self.file: str = file_name
        self.col: int = col
        
    def __str__(self) -> str:
        return f'Token({self.type}, {self.value})'