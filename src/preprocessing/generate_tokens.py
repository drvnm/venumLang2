from preprocessing.process import Lexer, remove_comments


def generate_tokens(path):
    file_content_raw = open(path).readlines()
    file_content = remove_comments(file_content_raw)

    lexer = Lexer(file_content, path)
    lexer.lex()

    lexer.generate_symbols()
    lexer.print_program()
    lexer.generate_blocks()

    return lexer.operations, lexer.function_names, lexer.variables, lexer.memory_index, lexer.constants
