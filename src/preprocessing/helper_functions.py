from typing import List
import sys


def remove_comments(lines: List[str]) -> List[str]:
    # remove comments
    new_lines = []

    for line in lines:
        line = line.split("//")[0]
        new_lines.append(line)

    # join lines
    return "".join(new_lines)

# shows error message and exits
def error(msg: str, line: int, file_name: str, col: int, line_content: str) -> None:    
    error_length = len(line_content.split(" ")[-1])
    print(f"File: {file_name}, line: {line + 1}, col: {col}")
    print(f"   Error: {msg}")
    print(f"   Line: {line_content}")
    print(f"         {(col - error_length) * ' ' }^")
    sys.exit(1)

