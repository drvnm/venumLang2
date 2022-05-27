import sys
from scanning.lexer import Lexer
from visitors.ast_printer import AstPrinter
from compiler.compiler import Compiler
from preproccesor.preprocessor import PreProcessor
from parsing.parser import *
from parsing.expressions import *


class Runner():
    has_error = False
    
    # this is a static method because i am planning to use
    # the runner class for error handling
    @staticmethod
    def run_file(path: str) -> None:
        file = open(path, 'r')
        source = file.readlines()
        pre_processor = PreProcessor(source)
        pre_processor.preprocess()
        source = pre_processor.final_source
        lexer = Lexer(source)
        lexer.scan()
        exprs = Parser(lexer.tokens).parse()
        compiler = Compiler()
        compiler.compile(exprs)

