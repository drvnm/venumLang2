import sys
from typing import Union
from intermediate.tokens import Token

def error(line: Union[Token, int], message: str):
    if isinstance(line, Token):
        if hasattr(line, 'file'):
            print(f'[FILE] {line.file}:{line.line}:{line.col}', file=sys.stderr)
            print(f'[LINE CONTENT] {line.line_content.strip()}', file=sys.stderr)
            print(f'\033[31;1m[ERROR]\033[0m {message}', file=sys.stderr)
            sys.exit(1)

    line = line.line if hasattr(line, 'line') else line
    print(f'[line {line}] \033[31;1mError\033[0m: {message}', file=sys.stderr)
    sys.exit(1)

def assert_error(condition: bool, line: Union[Token, int], message: str):
    if not condition:
        error(line, message)