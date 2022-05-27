import re
from typing import List
from scanning.error import error
from .env import PreEnv
from intermediate.lookup_tables import *


# preprocessor, takes string and passes output to scanner
class PreProcessor:
    def __init__(self, file_source: str):
        self.source_lines = file_source
        self.env = PreEnv()  # preprocessor data holder
        self.line_num = 0
        self.final_source = ''

    def expect(self, line: List[str], length: int, message: str) -> None:
        line_len = len(line)
        if line_len < length:
            error(self.line_num + 1, message)
        return line_len
    
    # parses a word to remove non alphanumeric characters
    def parse_line(self, word: str) -> List[str]:
        words = re.split(r'([\W ])', word)
        for idx, word in enumerate(words):
            if word in self.env.data:
                words[idx] = self.env.data[word]
        return words
        
    # defines a new macro
    def macro(self, splitted_line: List[str]) -> None:
        line_len = self.expect(splitted_line, 2, 'Invalid macro definition')
        macro_name = splitted_line[1].replace('\n', '')
        if line_len == 2:
            self.env.set(macro_name, '')
        else:
            macro_body = ' '.join(splitted_line[2:])
            macro_body = macro_body.replace('\n', '') # remove newline if any
            self.env.set(macro_name, macro_body)

    def import_file(self, splitted_line: List[str]) -> str:
        found_str = False
        for word in splitted_line:
            word = word.strip()
            if word.startswith('"') and word.endswith('"'):
                found_str = True
                break
        if not found_str:
            error(self.line_num + 1, 'Invalid import statement')
        file_name = word.replace('"', '') 
        try:           
            with open(file_name, 'r') as file:
                file_source = file.readlines()
                pre_processor = PreProcessor(file_source)
                pre_processor.preprocess()
                self.env.updata_from_env(pre_processor.env)
                return pre_processor.final_source
        except FileNotFoundError:
            error(self.line_num + 1, f'File {file_name} not found')


    def preprocess(self) -> None:
        for line_num, line in enumerate(self.source_lines):
            splitted_line = line.split(' ')
            self.line_num = line_num
            if splitted_line[0].startswith('@'):
                word = splitted_line[0][1:].replace('\n', '')
                if word == 'macro':
                    self.macro(splitted_line)
                    splitted_line = ['\n']
                elif word == 'import':
                    other_file_source = self.import_file(splitted_line)
                    splitted_line = [other_file_source]
                else:
                    error(self.line_num + 1, 'Invalid preprocessor directive')
            else:
                splitted_line = self.parse_line(' '.join(splitted_line))

            self.final_source += ''.join(splitted_line)
        
        # print('----')
        # print(self.final_source)

    
