from process import Lexer, remove_comments
from type_checker import TypeChecker
from executor import Executor
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <file_name> <output_file>")
        exit(1)
    
    file_name = sys.argv[1]
    output_file = sys.argv[2]
    # checks if path is valid
    if not os.path.isfile(file_name):
        print(f"File {file_name} does not exist")
        exit(1)

    file_content_raw = open(file_name).readlines()
    file_content = remove_comments(file_content_raw)
    
    lexer = Lexer(file_content, file_name)
    lexer.lex()
   
    lexer.generate_variables()
    lexer.print_program()
    lexer.generate_blocks()

    type_checker = TypeChecker(lexer.operations)
    # type_checker.check() # disabled for now...

    executor = Executor(lexer.operations, file_name, lexer.function_names, output_file)
    executor.execute()
