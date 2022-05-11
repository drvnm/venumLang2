# info
this subrepo will contain the code for the second venumlang compiler
the difference between this compiler and the first compiler will be the use of a recursive descent parser.

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