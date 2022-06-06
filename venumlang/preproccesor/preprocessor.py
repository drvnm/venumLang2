import os
import re
from typing import List
from venumlang.scanning.error import error
from .env import PreEnv
from venumlang.intermediate.lookup_tables import *


# preprocessor, takes string and passes output to scanner
class PreProcessor:
    def __init__(self, file_source: str, absolute_path: str):
        self.source_lines = file_source
        self.absolute_path = absolute_path
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
            macro_body = macro_body.replace('\n', '')  # remove newline if any
            self.env.set(macro_name, macro_body)

    def preprocess(self) -> None:
        for line_num, line in enumerate(self.source_lines):
            splitted_line = line.split(' ')
            self.line_num = line_num
            if splitted_line[0].startswith('@'):
                word = splitted_line[0][1:].replace('\n', '')
                if word == 'macro':
                    self.macro(splitted_line)
                    splitted_line = ['\n']
                else:
                    error(self.line_num + 1, 'Invalid preprocessor directive')
            else:
                splitted_line = self.parse_line(' '.join(splitted_line))

            self.final_source += ''.join(splitted_line)

        # print('----')
        # print(self.final_source)
