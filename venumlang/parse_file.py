import os
from typing import List
from venumlang.scanning.lexer import Lexer
from venumlang.scanning.lexer import Lexer
from venumlang.preproccesor.preprocessor import PreProcessor
from venumlang.parsing.parser import *
from venumlang.parsing.expressions import *
from venumlang.scanning.error import *

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