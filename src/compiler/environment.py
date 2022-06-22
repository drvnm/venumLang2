from typing import List
from parsing.statements import *
from scanning.error import assert_error
from intermediate.tokens import *
from intermediate.lookup_tables import *


# class that will hold data states
class Environment:
    memory_index = 0
    def __init__(self):
        self.enclosing = None

        self.variables = {}
        self.functions = {}
        self.arrays = {}
        self.structs = {}
    
    def define_string(self, var: VarStmt):
        name = var.name.lexeme
        assert_error(name not in self.variables, var.name, f'Variable {name} already defined')
        self.variables[name] = [Environment.memory_index, 'QWORD', True]
        Environment.memory_index += 8
    
    def define(self, var: VarStmt):
        # check if the variable is a string
        if var.type.type == tokens.STR:
            self.define_string(var)
            return
        name = var.name.lexeme
        size = var.size
        assert_error(name not in self.variables, var.name, f'Variable {name} already defined')
        word = size_to_word[size]
        self.variables[name] = [Environment.memory_index, word, False]
        Environment.memory_index += size

    # return memory index of variable and word
    def get(self, name: Token):
        if name.lexeme in self.variables:
            return self.variables[name.lexeme]
        else:
            assert_error(self.enclosing is not None, name, f'Variable {name.lexeme} not defined')
            return self.enclosing.get(name)
    
    # set environment for parent blocks
    def set_environment(self, enclosing: 'Environment'):
        self.enclosing = enclosing
        Environment.memory_index = Environment.memory_index
    
    # define function
    def define_function(self, function: FuncStmt):
        name = function.name.lexeme
        assert_error(name not in self.functions, function.name, f'Function {name} already defined')
        self.functions[name] = function
    
    # get function
    def get_function(self, name: Token) -> FuncStmt:
        if name.lexeme in self.functions:
            return self.functions[name.lexeme]
        else:
            assert_error(self.enclosing is not None, name, f'Function {name.lexeme} not defined')
            return self.enclosing.get_function(name)

    # defining arrays
    def define_array(self, arr: ArrayStmt):
        name = arr.name.lexeme
        assert_error(name not in self.variables, arr.name, f'Variable {name} already defined')
        self.variables[name] = [Environment.memory_index, arr, False]
        Environment.memory_index += arr.size

   