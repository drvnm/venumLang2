import sys
from scanning.lexer import Lexer
from visitors.ast_printer import AstPrinter
from compiler.compiler import Compiler
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

            expr = Parser(lexer.tokens).parse()
            compiler = Compiler()
            compiler.compile(expr)
            print(AstPrinter().print(expr))


    @staticmethod
    def run_file(path: str) -> None:
        file = open(path, 'r')
        source = file.read()

        lexer = Lexer(source)
        lexer.scan()
        exprs = Parser(lexer.tokens).parse()
        compiler = Compiler()
        compiler.compile(exprs)

        # print(lexer.tokens)
