import sys

def error(line: int, message: str):
    print(f'[line {line.line}] Error: {message}', file=sys.stderr)
    sys.exit(1)