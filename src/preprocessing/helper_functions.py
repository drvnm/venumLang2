from typing import List
import sys


def remove_comments(lines: List[str]) -> List[str]:
    # remove comments
    new_lines = []

    for line in lines:
        line = line.split("//")[0]
        new_lines.append(line)

    # join lines
    return "\n".join(new_lines)

# shows error message and exits
def error(msg: str, line: int, file_name: str, col: int) -> None:
    print(f"File: {file_name}, line: {line + 1}, col: {col}")
    print(f"   Error: {msg}")
    sys.exit(1)

