import sys
from scanning.lexer import Lexer
from scanning.lexer import Lexer
from visitors.ast_printer import AstPrinter
from compiler.compiler import Compiler
from preproccesor.preprocessor import PreProcessor
from parsing.parser import *
from parsing.expressions import *


def main():
    cmd_args = sys.argv[1:]
    if len(cmd_args) > 1 or len(cmd_args) == 0:
        print("Usage: python3 main.py <file_path>")
        sys.exit(1)

    elif len(cmd_args) == 1:
        file_path = cmd_args[0]
        file = open(file_path, 'r')
        source = file.readlines()
        pre_processor = PreProcessor(source)
        pre_processor.preprocess()
        source = pre_processor.final_source
        lexer = Lexer(source)
        lexer.scan()
        exprs = Parser(lexer.tokens).parse()
        compiler = Compiler()
        compiler.compile(exprs)
        
if __name__ == "__main__":
    main()
