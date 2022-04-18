from enum import Enum

operations = Enum('operations', """ 

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
            IF
            ELSE
            END
            WHILE
            FOR
            VAR
            IDENTIFIER
            WRITE
            LOAD
            FUNC
            RETURN
            CONTINUEF
            CONST
            STRUCT
            LOADARR
            WRITEARR

            HELPERS

            FUNC_NAME
            FUNC_CALL
            IN
            FUNC_END
            CONST_CALL
            CONST_DEF
            
            TYPES
            FLOAT
            INT
            STRING
            VARIABLE
            INT_8
            INT_16
            INT_32
            INT_64
            ARRAY
            CHAR

            SYSCALLS
            SYSCALL1
            SYSCALL2
            SYSCALL3
            SYSCALL4
            SYSCALL5
            SYSCALL6

            INTRINSICS
            POP
            SWAP
            EXIT

            PREPROCESSORS
            INCLUDE
            

            
                        """)


class Operation:
    def __init__(self, type_: operations,
                 value: any,
                 line: int,
                 file_name: str,
                 col: int
                 ) -> None:

        self.type: operations = type_
        self.value: any = value
        self.line: int = line
        self.file: str = file_name
        self.col: int = col

    def __str__(self) -> str:
        return f'Operation({self.type}, {self.value})'
