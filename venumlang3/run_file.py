import sys
from scanning.lexer import Lexer
from parsing.parser import *
from parsing.expressions import *

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

            parser = Parser(lexer.tokens + [Token(tokens.EOF, None, 0, 0)])
            expression = parser.parse()

            print(AstPrinter().print(expression))

            interpreter = Interpreter()
            result = interpreter.evaluate(expression)
            print(result)


            

    @staticmethod
    def run_file(path: str) -> None:
        file = open(path, 'r')
        source = file.read()

        lexer = Lexer(source)
        lexer.scan()
        print(lexer.tokens)

        file.close()
