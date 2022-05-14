# info
this subrepo will contain the code for the second venumlang compiler
the difference between this compiler and the first compiler will be the use of a recursive descent parser.

# roadmap checklist (for now)
- [X] recursive descent parser, with good grammar
- [X] variable declarations
- [X] function declarations
- [X] branching
- [X] loops
- [X] compiler
- [ ] native functions
- [ ] module system
- [ ] type checker
- [ ] OOP-like syntax
# types
At the moment, venumlang supports the following primitive types:
byte, short, int, long

# variables
```cpp
int x = 3 + 3; // bind 6 to x;
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
}

factorial(5); // should print 120
>> 120;
```

# table of operations
here is a pretty table of operations:
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
