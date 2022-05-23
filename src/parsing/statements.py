from abc import ABC, abstractmethod
from typing import List
from .expressions import *

class Stmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# represents a print statement like print <expr>;
class PrintStmt(Stmt):
    def __init__(self, expr: Expr):
        self.expr = expr
    
    def accept(self, visitor):
        visitor.visit_print_stmt(self)
    
# represents any expression that has side effect
class ExprStmt(Stmt):
    def __init__(self, expr: Expr):
        self.expr = expr
    
    def accept(self, visitor):
        visitor.visit_expr_stmt(self)

# represents a variable declaration like int x = <expr>;
class VarStmt(Stmt):
    def __init__(self, type: tokens, name: Token, expr: Expr, size: int):
        self.type = type
        self.name = name
        self.expr = expr
        self.size = size
    
    def accept(self, visitor):
        visitor.visit_var_stmt(self)

# represents a array declaration like int x[<expr>] = <expr>;
class ArrayStmt(Stmt):
    def __init__(self, type: tokens, name: Token, exprs: List[Expr], size: int):
        self.type = type
        self.name = name
        self.exprs = exprs
        self.size = size
    
    def accept(self, visitor):
        visitor.visit_array_stmt(self)

# represents a block of statements
class BlockStmt(Stmt):
    def __init__(self, statements: List[Stmt]):
        self.statements = statements

    def accept(self, visitor):
        visitor.visit_block_stmt(self)

# class that represents if statement, with elifs and else statements
class IfStmt(Stmt):
    def __init__(self, condition: Expr, then_branch: Stmt, elif_statements: List[Stmt], else_branch: Stmt):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
        self.elif_statements = elif_statements
    
    def accept(self, visitor):
        visitor.visit_if_stmt(self)

# class to represent while statements
class WhileStmt(Stmt):
    def __init__(self, condition: Expr, body: Stmt, label_index: int, end_index: int):
        self.condition = condition
        self.body = body
        self.label_index = label_index
        self.end_index = end_index
    
    def accept(self, visitor):
        visitor.visit_while_stmt(self)

# class to represent a break out of loop statement
class BreakStmt(Stmt):
    def __init__(self, label_index: int):
        self.label_index = label_index
    
    def accept(self, visitor):
        visitor.visit_break_stmt(self)

    
# class to represent a continue out of loop statement
class ContinueStmt(Stmt):
    def __init__(self, label_index: int):
        self.label_index = label_index
    
    def accept(self, visitor):
        visitor.visit_continue_stmt(self)


# represents a function declaration
class FuncStmt(Stmt):
    def __init__(self, name: Token, parameters: List[VarStmt], body: List[Stmt], return_type: tokens):
        self.name = name
        self.parameters = parameters
        self.body = body
        self.return_type = return_type
    
    def accept(self, visitor):
        visitor.visit_func_stmt(self)

# represents a syscall being made 
class SyscallStmt(Stmt):
    def __init__(self, syscall_number: int, args: List[Expr]):
        self.syscall_number = syscall_number
        self.args = args
    
    def accept(self, visitor):
        visitor.visit_syscall_stmt(self)
    
# represents a return statement
class ReturnStmt(Stmt):
    def __init__(self, value: Expr):
        self.value = value
    
    def accept(self, visitor):
        visitor.visit_return_stmt(self)

# represents a struct declaration
class StructStmt(Stmt):
    def __init__(self, name: Token, fields: List[VarStmt]):
        self.name = name
        self.fields = fields
    
    def accept(self, visitor):
        visitor.visit_struct_stmt(self)
    
# class to represent a inline assembly statement
class AsmStmt(Stmt):
    def __init__(self, assembly: List[Token]):
        self.assembly = assembly
    
    def accept(self, visitor):
        visitor.visit_asm_stmt(self)