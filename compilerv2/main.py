import sys
from scanning.lexer import Lexer
from run_file import *

if __name__ == "__main__":
    cmd_args = sys.argv[1:]
    if len(cmd_args) > 1:
        print("Usage: python3 main.py <file_name>")
        sys.exit(1)

    elif len(cmd_args) == 1:
        Runner.run_file(cmd_args[0])

    elif len(cmd_args) == 0:
        Runner.run_repl()
