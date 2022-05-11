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

    'byte': tokens.BYTE,	
    'short': tokens.SHORT,
    'int': tokens.INT,
    'long': tokens.LONG,
    'bool': tokens.BOOL,
}

type_to_size = {
    tokens.BYTE: 1,
    tokens.SHORT: 2,
    tokens.INT: 4,
    tokens.LONG: 8,
    tokens.BOOL: 1,
}

size_to_word = {
    1: 'BYTE',
    2: 'WORD',
    4: 'DWORD',
    8: 'QWORD',
}

word_to_register = {
    'BYTE': 'AL',
    'WORD': 'AX',
    'DWORD': 'EAX',
    'QWORD': 'RAX',
}