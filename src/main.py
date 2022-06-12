import argparse
import os
from scanning.lexer import Lexer
from scanning.lexer import Lexer
from compiler.compiler import Compiler
from pre_processing.preprocessor import PreProcessor
from parsing.parser import *
from parsing.expressions import *
from typechecking.type_checker import *
from config_options import ConfigOptions
import toml

parser = argparse.ArgumentParser()
parser.add_argument("input", help="The input file to compile")
parser.add_argument("-o", "--output", help="The output file to write to", default="output")
parser.add_argument("-r", "--run", help="Run compiled code after compilation finishes", action="store_true", 
                    default=False, dest="do_run")


def main():
    config = {}
    if os.path.isfile("config.toml"):
        config = toml.load("config.toml")

    options = ConfigOptions(config)

    args = parser.parse_args()
    file_path = args.input
    with open(file_path, 'r') as f:
        source = f.read()
    
    absolute_path = os.path.abspath(file_path)
    pre_processor = PreProcessor(source, absolute_path, options)
    pre_processor.preprocess()
    source = pre_processor.source
    lexer = Lexer(source, absolute_path)
    lexer.scan()

    exprs = Parser(lexer.tokens).parse()

    # type_checker = TypeChecker(exprs)
    # type_checker.execute()



    compiler = Compiler(file_path, args.output, args.do_run)
    compiler.compile(exprs)


if __name__ == "__main__":
    main()
