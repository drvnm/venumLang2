from .tokens import tokens

single_char_tokens = {
    '(': tokens.LEFT_PAREN,
    ')': tokens.RIGHT_PAREN,
    '{': tokens.LEFT_BRACE,
    '}': tokens.RIGHT_BRACE,
    ',': tokens.COMMA,
    '.': tokens.DOT,
    '-': tokens.MINUS,
    '+': tokens.PLUS,
    ';': tokens.SEMICOLON,
    '*': tokens.STAR,
    '&' : tokens.AMPERSAND,
    '%' : tokens.PERCENT, 
    '[': tokens.LEFT_SQUARE,
    ']': tokens.RIGHT_SQUARE,
}

two_char_tokens = {
    '!': '=',
    '=': '=',
    '<': '=',
    '>': '=',
    '|': '|',
    '&': '&',
    '+': '=',
    '-': '=',
    '*': '=',
    '/': '=',
}

optional_to_token = {
    '!=': tokens.BANG_EQUAL,
    '==': tokens.EQUAL_EQUAL,
    '<=': tokens.LESS_EQUAL,
    '>=': tokens.GREATER_EQUAL,
    '=': tokens.EQUAL,
    '<': tokens.LESS,
    '>': tokens.GREATER,
    '!': tokens.BANG,
    '||': tokens.OR,
    '&&': tokens.AND,
    '+=': tokens.PLUS_EQUAL,
    '-=': tokens.MINUS_EQUAL,
    '*=': tokens.STAR_EQUAL,
    '/=': tokens.SLASH_EQUAL,
}


word_to_keyword = {
    'and': tokens.AND,
    'class': tokens.CLASS,
    'syscall': tokens.SYSCALL,
    'else': tokens.ELSE,
    'false': tokens.FALSE,
    'for': tokens.FOR,
    'if': tokens.IF,
    'null': tokens.NULL,
    'or': tokens.OR,
    'print': tokens.PRINT,
    'return': tokens.RETURN,
    'super': tokens.SUPER,
    'this': tokens.THIS,
    'true': tokens.TRUE,
    'while': tokens.WHILE,
    'elif': tokens.ELIF,
    'continue': tokens.CONTINUE,
    'break': tokens.BREAK,
    'func': tokens.FUNC,
    'byte': tokens.BYTE,	
    'short': tokens.SHORT,
    'int': tokens.INT,
    'long': tokens.LONG,
    'bool': tokens.BOOL,
    'str': tokens.STR,
    'struct': tokens.STRUCT,
    'asm': tokens.ASM,
}

type_to_size = {
    tokens.BYTE: 1,
    tokens.SHORT: 2,
    tokens.INT: 4,
    tokens.LONG: 8,
    tokens.BOOL: 1,
    tokens.STR: 8,
}

size_to_word = {
    1: 'BYTE',
    2: 'WORD',
    4: 'DWORD',
    8: 'QWORD',
}

word_to_register = {
    'BYTE': 'al',
    'WORD': 'ax',
    'DWORD': 'eax',
    'QWORD': 'rax',
}

word_to_register_size = {
    'BYTErax': 'al',
    'WORDrax': 'ax',
    'DWORDrax': 'eax',
    'QWORDrax': 'rax',
    'BYTErdi': 'dil',
    'WORDrdi': 'di',
    'DWORDrdi': 'edi',
    'QWORDrdi': 'rdi',
    'BYTErsi': 'sil',
    'WORDrsi': 'si',
    'DWORDrsi': 'esi',
    'QWORDrsi': 'rsi',
    'BYTErdx': 'dl',
    'WORDrdx': 'dx',
    'DWORDrdx': 'edx',
    'QWORDrdx': 'rdx',
    'BYTErcx': 'cl',
    'WORDrcx': 'cx',
    'DWORDrcx': 'ecx',
    'QWORDrcx': 'rcx',
    'BYTEr8': 'r8b',
    'WORDr8': 'r8w',
    'DWORDr8': 'r8d',
    'QWORDr8': 'r8',
    'BYTEr9': 'r9b',
    'WORDr9': 'r9w',
    'DWORDr9': 'r9d',
    'QWORDr9': 'r9',
    'BYTEr10': 'r10b',
    'WORDr10': 'r10w',
    'DWORDr10': 'r10d',
    'QWORDr10': 'r10',
}

preprocessing_words = ['import', 'define', 'ifdef', 'endif']