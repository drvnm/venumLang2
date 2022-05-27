import argparse
import os
from scanning.lexer import Lexer
from scanning.lexer import Lexer
from compiler.compiler import Compiler
from preproccesor.preprocessor import PreProcessor
from parsing.parser import *
from parsing.expressions import *

parser = argparse.ArgumentParser()
parser.add_argument("input", help="The input file to compile")
parser.add_argument("-o", "--output", help="The output file to write to", default="output")

def main():
    args = parser.parse_args()
    file_path = args.input 
    file = open(file_path, 'r')
    source = file.readlines()
    absolute_path = os.path.abspath(file_path)
    pre_processor = PreProcessor(source, absolute_path)
    pre_processor.preprocess()
    source = pre_processor.final_source
    lexer = Lexer(source, absolute_path)
    lexer.scan()
    exprs = Parser(lexer.tokens).parse()
    compiler = Compiler(file_path, args.output)
    compiler.compile(exprs)


if __name__ == "__main__":
    main()
