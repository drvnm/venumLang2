import sys
from scanning.lexer import Lexer
from interpreter.interpreter import Interpreter
from parsing.parser import *
from parsing.expressions import *
from visitors.ast_printer import *

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
            
            exprs = Parser(lexer.tokens).parse()
            interpreter = Interpreter()
            interpreter.execute(exprs)
            
            
    @staticmethod
    def run_file(path: str) -> None:
        file = open(path, 'r')
        source = file.read()

        lexer = Lexer(source)
        lexer.scan()
            
        exprs = Parser(lexer.tokens).parse()
        interpreter = Interpreter()
        interpreter.execute(exprs)
        
        file.close()
