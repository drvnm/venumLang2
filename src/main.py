import argparse
import os
from scanning.lexer import Lexer
from scanning.lexer import Lexer
from compiler.compiler import Compiler
from preproccesor.preprocessor import PreProcessor
from parsing.parser import *
from parsing.expressions import *
from typechecking.type_checker import *

parser = argparse.ArgumentParser()
parser.add_argument("input", help="The input file to compile")
parser.add_argument("-o", "--output", help="The output file to write to", default="output")
parser.add_argument("-I", dest="include_path", help="Include path for imports, comma separated", default="")


def main():
    args = parser.parse_args()
    file_path = args.input

    with open(file_path, 'r') as f:
        source = f.readlines()
    
    absolute_path = os.path.abspath(file_path)
    pre_processor = PreProcessor(source, absolute_path)
    pre_processor.preprocess()
    source = pre_processor.final_source
    lexer = Lexer(source, absolute_path)
    lexer.scan()
    exprs = Parser(lexer.tokens).parse()

    # type_checker = TypeChecker(exprs)
    # type_checker.execute()

    include_path = ['.']+args.include_path.split(',') if args.include_path else ['.']
    print(f"{include_path=}")
    for path in include_path:
        if not os.path.isdir(path):
            print(f"{path}: No such file or directory", file=sys.stderr)
            sys.exit(1)

    compiler = Compiler(file_path, include_path, args.output)
    compiler.compile(exprs)


if __name__ == "__main__":
    main()
