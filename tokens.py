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
            RETURN
            CONTINUEF

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
            INT_8
            INT_16
            INT_32
            INT_64

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
            
                        """)

syscall_table = [operations.SYSCALL1, operations.SYSCALL2, operations.SYSCALL3, operations.SYSCALL4, operations.SYSCALL5, operations.SYSCALL6]
operator_table = {
    "+": operations.PLUS,
    "-": operations.MIN,
    "*": operations.MUL,
    "/": operations.DIV,
    ">": operations.GT,
    ">=": operations.GTE,
    "<": operations.LT,
    "<=": operations.LTE,
    "==": operations.EQ,
    "!=": operations.NEQ,	
    "%": operations.MOD,
    "&&": operations.DOUBLE_AND
}

matching_operations = {
    operations.INT: operations.INT_PUSH,
    operations.FLOAT: operations.FLOAT_PUSH,
    operations.STRING: operations.STRING_PUSH,
}

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