"""
Btw this test code was mostly written for farkon00/cont repo.
But it's owner(farkon00) granted permission with MIT License to use it.
And this code was added orginally by him.
"""

import os
import subprocess
import pytest

tests = os.listdir("tests")

try:
    os.mkdir("tests/results")
except FileExistsError:
    tests.remove("results")
try:
    os.mkdir("tests/temp")
except FileExistsError:
    tests.remove("temp")

@pytest.mark.parametrize("test_name", tests)
def test(test_name):
    with open(f"tests/{test_name}", "r") as f:
        test = f.read()
    
    parts = test.split("\n:\n")

    with open("tests/temp/code.vlang", "w") as f:
        f.write(parts[0])
    with open("tests/temp/stdin", "w") as f:
        if len(parts) > 2:
            f.write(parts[2])
    exp_stdout = parts[1]
    if len(parts) > 3:
        exp_stderr = parts[3]
    else:
        exp_stderr = ""

    stdout = open(f"tests/results/{test_name}_stdout", "w") 
    stderr = open(f"tests/results/{test_name}_stderr", "w")
    stdin = open("tests/temp/stdin", "r")

    subprocess.run(["python3", "src/main.py", "tests/temp/code.vlang", "-r", "-s"], stdout=stdout, stderr=stderr, stdin=stdin)

    stdout.close()
    stderr.close()
    stdin.close()

    with open(f"tests/results/{test_name}_stdout", "r") as f:
        stdout_content = f.read()
    with open(f"tests/results/{test_name}_stderr", "r") as f:
        stderr_content = f.read()

    assert stdout_content == exp_stdout
    assert stderr_content == exp_stderr