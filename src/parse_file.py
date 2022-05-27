import os
from typing import List
from scanning.lexer import Lexer
from scanning.lexer import Lexer
from preproccesor.preprocessor import PreProcessor
from parsing.parser import *
from parsing.expressions import *

def get_file_ast(current_file: str, file_path: str) -> List[Token]:
    file_path = os.path.join(os.path.dirname(current_file), file_path)
    print(file_path)
    file = open(file_path, 'r')
    source = file.readlines()
    absolute_path = os.path.abspath(file_path)
    pre_processor = PreProcessor(source, absolute_path)
    pre_processor.preprocess()
    source = pre_processor.final_source
    lexer = Lexer(source, absolute_path)
    lexer.scan()
    parser = Parser(lexer.tokens)
    ast = parser.parse()
    return ast


