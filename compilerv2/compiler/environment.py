from parsing.statements import VarStmt
from scanning.error import error
from intermediate.tokens import *
from intermediate.lookup_tables import *

# class that will hold data states
class Environment:
    def __init__(self):
        self.variables = {}
        self.memory_index = 0
        self.enclosing = None
    
    def define(self, var: VarStmt):
        name = var.name.lexeme
        size = var.size
        if name in self.variables:
            error(var.name, f'Variable {name} already defined')
        word = size_to_word[size]
        self.variables[name] = [self.memory_index, word]
        self.memory_index += size

    # return memory index of variable
    def get(self, name: Token) -> int:
        if name.lexeme in self.variables:
            return self.variables[name.lexeme]
        else:
            if self.enclosing != None:
                return self.enclosing.get(name)
            else:
                error(name, f'Variable {name.lexeme} not defined')
    
    # set environment for parent blocks
    def set_environment(self, enclosing: 'Environment'):
        self.enclosing = enclosing
        self.memory_index = enclosing.memory_index

