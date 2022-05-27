
from sys import builtin_module_names
from preprocessing.operations import operations


syscall_table = [operations.SYSCALL2, operations.SYSCALL3,
                 operations.SYSCALL4, operations.SYSCALL5, operations.SYSCALL6
                 ]

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
    "&&": operations.DOUBLE_AND,
    "#include": operations.INCLUDE,
}

matching_operations = {
    operations.INT: operations.INT_PUSH,
    operations.FLOAT: operations.FLOAT_PUSH,
    operations.STRING: operations.STRING_PUSH,
}

SIZE_DICT = {
    operations.INT: "BYTE",
    operations.INT_8: "BYTE",
    operations.INT_16: "WORD",
    operations.INT_32: "DWORD",
    operations.INT_64: "QWORD",
    operations.CHAR: "BYTE",
}

SIZE_REG_DICT = {
    operations.INT_8: "AL",
    operations.INT_16: "AX",
    operations.INT_32: "EAX",
    operations.INT_64: "RAX",
    operations.CHAR: "AL",
}

type_size = {
    operations.INT: 8,
    operations.INT_8: 1,
    operations.INT_16: 2,
    operations.INT_32: 4,
    operations.INT_64: 8,
    operations.CHAR: 1,
}

builtin_types = ["int", "int_8", "int_16", "int_32", "int_64", "char"]
