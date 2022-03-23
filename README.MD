# VLANG
This is my toy language, heavily inspired by [Porth](https://gitlab.com/tsoding/porth)

This is a statically typed language written in python, and compiles to x64 assembly!

## TODO'S
- [x] Numerical values
- [x] Print function
- [X] Strings
- [X] Conditionals 
- [X] Loops
- [ ] Functions
- [X] Memory
- [ ] Standard library

# variables
#### Syntax will be improved
```js
// also supports! comments
var x int // provide a type (int float or string for now)

2 x write // writes 2 into x
x load // loads the value stored in x ontop of the stack
```	

# if statements and loops
```js
5 5 == if 
    "5 is indeed equal to 5" puts

else
    // some code
end

while x 5 < do 
    "woah" puts
     x load 1 + x write
end
```

# stack operations
```js
1 1 
// LIST OF VALID OPERATIONS:
+ - * / % > >= < <= ==
```

