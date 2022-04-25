import sys
from scanning.lexer import Lexer


class Runner():
    has_error = False

    @staticmethod
    def run_repl() -> None:
        while True:
            source = input('> ')
            if source == 'exit()':
                sys.exit()
            lexer = Lexer(source)
            lexer.scan()
            print(lexer.tokens)

    @staticmethod
    def run_file(path: str) -> None:
        file = open(path, 'r')
        source = file.read()

        lexer = Lexer(source)
        lexer.scan()
        print(lexer.tokens)

        file.close()
