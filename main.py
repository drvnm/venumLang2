from process import Lexer, remove_comments
from type_checker import TypeChecker
from executor import Executor
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <filename>")
        exit(1)
    
    file_name = sys.argv[1]

    file_content_raw = open(file_name).readlines()
    file_content = remove_comments(file_content_raw)
    
    lexer = Lexer(file_content, file_name)
    lexer.lex()
    lexer.print_tokens()

    type_checker = TypeChecker(lexer.tokens)
    type_checker.check()

    executor = Executor(lexer.tokens, file_name)
    executor.execute()
