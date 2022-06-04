import os
from typing import List
from scanning.lexer import Lexer
from scanning.lexer import Lexer
from preproccesor.preprocessor import PreProcessor
from parsing.parser import *
from parsing.expressions import *
from scanning.error import *

def get_file_ast(file_path: str) -> List[Token]:
    print(file_path)

    try:
        with open(file_path, 'r') as f:
            source = f.readlines()
    except FileNotFoundError:
        error("...", f"File '{file_path}' not found.")
    
    absolute_path = os.path.abspath(file_path)
    pre_processor = PreProcessor(source, absolute_path)
    pre_processor.preprocess()
    source = pre_processor.final_source
    lexer = Lexer(source, absolute_path)
    lexer.scan()
    parser = Parser(lexer.tokens)
    ast = parser.parse()
    return ast