# Join our discord!
[![Discord](https://badgen.net/badge/icon/discord?icon=discord&label)](https://discord.gg/WtXXdE2c3q)


# Installing venumLang
install venumlang via PIP: NOTE: I advise you to install by cloning this repo, because the pypi package is not actively being updated.
```
pip install venumLang==0.1.0
venumlang <file_path>
```
Or, clone the repo:
```
git clone https://github.com/darealvenum/venumLang2
python3 main.py <file_name>
```

# types
At the moment, venumlang supports the following primitive types:
byte, short, int, long, str, bool, void (return type) and arrays of these types.

# variables
venumlang has some native types and arrays. For now, arrays are only 1-dimensional. The size of an array also has to be a number.
```cpp
int x = 3 + 3; // bind 6 to x;
int arr[100];
int arr2[2] = {1, 2}; 
```

### memory address of and dereferencing
```cpp
print &x; // prints the memory address of x
x = *&x; // dereferences x and assigns it to x
```

# shadowing and scoping
in venumlang, variables can be shadowed in inner scopes.
```cpp
int x = 2000;
{
    int x = 3000;
    print x; // prints 3000
}
print x; // prints 2000
```

# branching 
venumlang has support for if, elif, and else statements:
```cpp
short x = 20 + 20 * 2;
if(x == 20) {
    print 1;
}
else if(x == 40) {
    print 2;
}
else {
    print 3; // will print 3
}
```

# loops
venumlang has support for while and for loops:
```cpp
short x = 0;
while(x < 10) {
    print x;
    x = x + 1;
}
```
```cpp
for(short x = 0; x < 10; x += 1) {
    print x;
}
```

# functions
venumlang has support for functions:
```cpp
func int factorial(int n) {
  int fact = 1;
  for (int i = 1; i <= n; i += 1) {
    fact *= i;
  }
  print fact;
  return fact;
}

factorial(5); // should print 120
>> 120;
```

# inline assembly
venumlang has support for inline assembly:
```cpp
short x = 100;
asm {
    "mov ax, WORD $x" // use $ to get the value of a variable
    "mov rax, &x" // use & to get the memory address of x
}
```
# making system calls
To interact with the OS, venumlang has systemcall statements (you could also use inline asm)
```cpp
syscall <id> <first param>, <second param> ...
```

# macros (and importing files)
venumlang has support for 1 lined macros:
```python
@macro x 12 * 2 + 34 + 420 * 69
print x;
>> 29038

@include "stdlib/io.vlang"; // copies file into current file
````

# table of operations
| Operation | Description |
| :-------: | :--------: |
| + | addition |
| - | subtraction |
| * | multiplication |
| / | division |
| % | modulus |
| == | equality |
| != | inequality |
| < | less than |
| > | greater than |
| <= | less than or equal to |
| >= | greater than or equal to |
| && | logical and (TODO) |
| || | logical or (TODO) |
| ! | logical not |
| = | assignment |
| += | addition assignment |
| -= | subtraction assignment |
| *= | multiplication assignment |
| /= | division assignment |
| & | address of |
| * | dereference |


# roadmap checklist (for now)
- [X] recursive descent parser, with good grammar
- [X] variable declarations
- [X] function declarations
- [X] branching
- [X] loops
- [X] compiler
- [X] module system?
- [X] type checker?
- [ ] OOP-like syntax