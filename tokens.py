from enum import Enum

tokens = Enum('tokens', """ 

            LITERALS
            INT_PUSH
            FLOAT_PUSH
            STRING_PUSH

            OPERATORS
            PLUS
            MIN
            MUL
            DIV
            GT
            GTE
            LT
            LTE
            EQ
            NEQ
            COPY
            MOD
            DOUBLE_AND

            KEYWORDS
            PRINT
            DO
            PUTS
            IFF
            ELSEF
            END
            WHILEF
            FORF
            VAR
            IDENTIFIER
            WRITE
            LOAD
            FUNC

            HELPERS
            FUNC_NAME
            FUNC_CALL
            IN
            FUNC_END

            TYPES
            FLOAT
            INT
            STRING
            VARIABLE
            

                        """)

operator_table = {
    "+": tokens.PLUS,
    "-": tokens.MIN,
    "*": tokens.MUL,
    "/": tokens.DIV,
    ">": tokens.GT,
    ">=": tokens.GTE,
    "<": tokens.LT,
    "<=": tokens.LTE,
    "==": tokens.EQ,
    "!=": tokens.NEQ,	
    "%": tokens.MOD,
    "&&": tokens.DOUBLE_AND
}

matching_tokens = {
    tokens.INT: tokens.INT_PUSH,
    tokens.FLOAT: tokens.FLOAT_PUSH,
    tokens.STRING: tokens.STRING_PUSH,
}



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