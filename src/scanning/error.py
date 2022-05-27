import sys
from typing import Union
from intermediate.tokens import Token

def error(line: Union[Token, int], message: str):
    if isinstance(line, Token):
        if hasattr(line, 'file'):
            index = " " * line.col
            print(line.col)
            print(f'File: {line.file}')
            print(f'[line {line.line}, col: {line.col}]')
            print(f'Line content: {line.line_content.strip()}', file=sys.stderr)
            print(f'Error: {message}', file=sys.stderr)
            sys.exit(1)

    line = line.line if hasattr(line, 'line') else line
    print(f'[line {line}] Error: {message}', file=sys.stderr)
    sys.exit(1)