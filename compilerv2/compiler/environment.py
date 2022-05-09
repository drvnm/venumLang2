from pyrsistent import v
from parsing.statements import VarStmt
from scanning.error import error
from intermediate.tokens import *

# class that will hold data states
class Environment:
    def __init__(self):
        self.variables = {}
        self.memory_index = 0
    
    def define(self, var: VarStmt, value: any):
        name = var.name.lexeme
        size = var.size
        if name in self.variables:
            error(name, f'Variable {name} already defined')
        self.variables[name] = [value, size]

    
    def get_(self, name: Token):
        if name.lexeme in self.variables:
            return self.variables[name.lexeme][0]
        error(name, f'Undefined variable {name.lexeme}')