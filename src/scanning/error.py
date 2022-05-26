import sys

def error(line: int, message: str):
    line = line.line if hasattr(line, 'line') else line
    print(f'[line {line}] Error: {message}', file=sys.stderr)
    sys.exit(1)