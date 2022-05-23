from typing import List
from parsing.statements import *
from scanning.error import error
from intermediate.tokens import *
from intermediate.lookup_tables import *

class DataHolder:
    def __init__(self, type: tokens, name: Token, expr: Expr, size: int):
        self.type = type
        self.name = name
        self.size = size

class StructData(DataHolder):
    def __init__(self, name: Token, members: List[DataHolder]):
        self.name = name
        self.members = members

class DataDeclr:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

class StructDeclr(DataDeclr):
    def __init__(self, name: str, size: int, members: List[DataDeclr]):
        super().__init__(name, size)
        self.members = members

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
        if name in self.variables:
            error(var.name, f'Variable {name} already defined')
        self.variables[name] = [Environment.memory_index, 'QWORD', True]
        Environment.memory_index += 8
    
    def define(self, var: VarStmt):
        # check if the variable is a string
        if var.type.type == tokens.STR:
            self.define_string(var)
            return
        name = var.name.lexeme
        size = var.size
        if name in self.variables:
            error(var.name, f'Variable {name} already defined')
        word = size_to_word[size]
        self.variables[name] = [Environment.memory_index, word, False]
        Environment.memory_index += size

    # return memory index of variable and word
    def get(self, name: Token):
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
        Environment.memory_index = Environment.memory_index
    
    # define function
    def define_function(self, function: FuncStmt):
        name = function.name.lexeme
        if name in self.functions:
            error(function.name, f'Function {name} already defined')
        self.functions[name] = function
    
    # get function
    def get_function(self, name: Token) -> FuncStmt:
        if name.lexeme in self.functions:
            return self.functions[name.lexeme]
        else:
            if self.enclosing != None:
                return self.enclosing.get_function(name)
            else:
                error(name, f'Function {name.lexeme} not defined')

    # defining arrays
    def define_array(self, arr: ArrayStmt):
        name = arr.name.lexeme
        if name in self.variables:
            error(arr.name, f'Variable {name} already defined')
        self.variables[name] = [Environment.memory_index, arr, False]
        Environment.memory_index += arr.size

    # define struct
    def define_struct(self, struct: StructStmt):
        size = sum([type_to_size[nam_tok.type.type] for nam_tok in struct.fields])
        struct_object = StructDeclr(struct.name.lexeme, size, struct.fields)
        self.structs[struct.name.lexeme] = struct_object
        