import subprocess
from typing import List
from .environment import Environment
from visitors.visitor import *
from parsing.statements import *
from parsing.expressions import *
from intermediate.tokens import *
from intermediate.lookup_tables import *


class Compiler(ExprVisitor, StmtVisitor):
    def __init__(self):
        self.file = open("output.asm", "w")
        self.output_file = "output"
        self.environment = Environment()
        self.mem_size = 64_00

    # writes line to asm file
    def write(self, line: str, indent: int = True):
        indent = "  " if indent else ""
        self.file.write(f" {indent}{line}\n")

    # writes begin of asm file
    def write_header(self):
        self.write("section .text", False)
        self.write("global _start")
        self.write("section .text")
        self.write("   global _start")

        self.write("print:")
        self.write("   push    rbp")
        self.write("   mov     rbp, rsp")
        self.write("   sub     rsp, 64")
        self.write("   mov     DWORD   [rbp-52], edi")
        self.write("   mov     DWORD   [rbp-4], 1")
        self.write("   mov     eax, DWORD   [rbp-4]")
        self.write("   movsx   rdx, eax")
        self.write("   mov     eax, 32")
        self.write("   sub     rax, rdx")
        self.write("   mov     BYTE   [rbp-48+rax], 10")
        self.write(".L2:")
        self.write("   mov     edx, DWORD   [rbp-52]")
        self.write("   movsx   rax, edx")
        self.write("   imul    rax, rax, 1717986919")
        self.write("   shr     rax, 32")
        self.write("   sar     eax, 2")
        self.write("   mov     esi, edx")
        self.write("   sar     esi, 31")
        self.write("   sub     eax, esi")
        self.write("   mov     ecx, eax")
        self.write("   mov     eax, ecx")
        self.write("   sal     eax, 2")
        self.write("   add     eax, ecx")
        self.write("   add     eax, eax")
        self.write("   mov     ecx, edx")
        self.write("   sub     ecx, eax")
        self.write("   mov     eax, ecx")
        self.write("   lea     ecx, [rax+48]")
        self.write("   mov     eax, DWORD   [rbp-4]")
        self.write("   movsx   rdx, eax")
        self.write("   mov     eax, 31")
        self.write("   sub     rax, rdx")
        self.write("   mov     edx, ecx")
        self.write("   mov     BYTE   [rbp-48+rax], dl")
        self.write("   add     DWORD   [rbp-4], 1")
        self.write("   mov     eax, DWORD   [rbp-52]")
        self.write("   movsx   rdx, eax")
        self.write("   imul    rdx, rdx, 1717986919")
        self.write("   shr     rdx, 32")
        self.write("   sar     edx, 2")
        self.write("   sar     eax, 31")
        self.write("   mov     ecx, eax")
        self.write("   mov     eax, edx")
        self.write("   sub     eax, ecx")
        self.write("   mov     DWORD   [rbp-52], eax")
        self.write("   cmp     DWORD   [rbp-52], 0")
        self.write("   jg      .L2")
        self.write("   mov     eax, DWORD   [rbp-4]")
        self.write("   cdqe")
        self.write("   mov     edx, DWORD   [rbp-4]")
        self.write("   movsx   rdx, edx")
        self.write("   mov     ecx, 32")
        self.write("   sub     rcx, rdx")
        self.write("   lea     rdx, [rbp-48]")
        self.write("   add     rcx, rdx")
        self.write("   mov     rdx, rax")
        self.write("   mov     rsi, rcx")
        self.write("   mov     edi, 1")
        self.write("   mov     rax, 1")
        self.write("   syscall")
        self.write("   nop")
        self.write("   leave")
        self.write("   ret")
        self.write("_start:", False)

    # writes end of asm file, calls exit system call
    def write_footer(self):
        self.write("; end of program")
        self.write("mov rax, 60")
        self.write("mov rdi, 0")
        self.write("syscall")

        # section for variables
        self.write("section .bss", False)
        self.write(f"MEMORY: resb {self.mem_size}")

    def compile(self, statements: List[Stmt]):
        self.write_header()
        for statement in statements:
            statement.accept(self)
        self.write_footer()
        self.file.close()

        # compile and link
        subprocess.run(["nasm", "-f", "elf64", f"{self.output_file}.asm"])
        subprocess.run(
            ["ld", "-o", f"{self.output_file}", f"{self.output_file}.o"])

    def execute(self, expr: Expr):
        expr.accept(self)

    def visit_literal_expr(self, expr: LiteralExpr):
        literal = expr.value.literal if isinstance(
            expr.value, Token) else expr.value
        if isinstance(literal, bool):
            literal = 1 if literal else 0
        self.write(f"push {literal}")

    def visit_unary_expr(self, unary_expr: UnaryExpr):
        self.execute(unary_expr.right)
        if unary_expr.operator.type == tokens.MINUS:
            self.write(f"pop rax ; negate top of stack")
            self.write(f"neg rax")
            self.write(f"push rax")
        elif unary_expr.operator.type == tokens.BANG:
            self.write(f"pop rax ; logical NOT top of stack")
            self.write(f"xor rax, 1")
            self.write(f"push rax")

    def visit_grouping_expr(self, grouping_expr: GroupingExpr):
        self.execute(grouping_expr.expression)

    def visit_binary_expr(self, binary_expr: BinaryExpr):
        self.execute(binary_expr.right)
        self.execute(binary_expr.left)

        if binary_expr.operator.type == tokens.MINUS:
            self.write(f"pop rax ; subtract right from left")
            self.write(f"pop rbx")
            self.write(f"sub rax, rbx")
            self.write(f"push rax")
        elif binary_expr.operator.type == tokens.PLUS:
            self.write(f"pop rax ; add right to left")
            self.write(f"pop rbx")
            self.write(f"add rax, rbx")
            self.write(f"push rax")
        elif binary_expr.operator.type == tokens.SLASH:
            self.write(f"pop rax ; divide left by right")
            self.write(f"pop rbx")
            self.write(f"div rbx")
            self.write(f"push rax")
        elif binary_expr.operator.type == tokens.STAR:
            self.write(f"pop rax ; multiply left by right")
            self.write(f"pop rbx")
            self.write(f"mul rbx")
            self.write(f"push rax")
        elif binary_expr.operator.type == tokens.GREATER:
            self.write(f"pop rax ; compare left to right")
            self.write(f"pop rbx")
            self.write(f"cmp rax, rbx")
        elif binary_expr.operator.type == tokens.GREATER_EQUAL:
            self.write(f"pop rax ; compare left to right")
            self.write(f"pop rbx")
            self.write(f"cmp rax, rbx")
        elif binary_expr.operator.type == tokens.LESS:
            self.write(f"pop rax ; compare left to right")
            self.write(f"pop rbx")
            self.write(f"cmp rax, rbx")
        elif binary_expr.operator.type == tokens.LESS_EQUAL:
            self.write(f"pop rax ; compare left to right")
            self.write(f"pop rbx")
            self.write(f"cmp rax, rbx")
        elif binary_expr.operator.type == tokens.BANG_EQUAL:
            self.write(f"pop rax ; compare left to right")
            self.write(f"pop rbx")
            self.write(f"cmp rax, rbx")
        elif binary_expr.operator.type == tokens.EQUAL_EQUAL:
            self.write(f"pop rax ; compare left to right")
            self.write(f"pop rbx")
            self.write(f"cmp rax, rbx")

    def visit_print_stmt(self, print_stmt: PrintStmt):
        self.execute(print_stmt.expr)

        # call print function
        self.write("pop rdi ; print statement")
        self.write("call print")

    def visit_expr_stmt(self, expr_stmt: ExprStmt):
        self.execute(expr_stmt.expr)

    # stores a variable in .bss
    def visit_var_stmt(self, var_stmt: VarStmt):
        if var_stmt.expr is not None:
            self.execute(var_stmt.expr)
            self.write(f"pop rax ; store variable {var_stmt.name.lexeme}")
        else:
            self.write(f"mov rax, 0 ; store variable {var_stmt.name.lexeme}")
        self.environment.define(var_stmt) # calculate address
        start_index, word = self.environment.get(var_stmt.name)
        self.write(f"mov [MEMORY + {start_index}], rax")

    # loads a variable from .bss
    def visit_var_expr(self, var_expr: VarExpr):
        start_index, word = self.environment.get(var_expr.name)
        register = word_to_register[word]
        self.write("xor rax, rax")
        self.write(f"mov {register}, {word} [MEMORY + {start_index}]")
        self.write(f"push rax")
    
    # handle references
    def visit_var_to_pointer_expr(self, var_to_pointer_expr: VarToPointerExpr):
        start_index, word = self.environment.get(var_to_pointer_expr.name)
        self.write(f"mov rax, MEMORY + {start_index}")
        self.write(f"push rax")

    # handle dereference (unsafe code LOL)
    def visit_dereference_expr(self, dereference_expr: DereferenceExpr):
        self.execute(dereference_expr.expr)
        # push value at memory address of top of stack
        self.write("xor rax, rax")
        self.write("pop rax")
        self.write("mov rax, [rax]")
        self.write("push rax")

    # handle assignment types
    def visit_assignment_expr(self, assign_expr: AssignmentExpr):
        self.execute(assign_expr.value)
        operator = assign_expr.operator.type
        start_index, word = self.environment.get(assign_expr.name)
        
        self.write(f"xor rax, rax ; assign value to variable {assign_expr.name.lexeme}")
        self.write("pop rax")
        if operator == tokens.EQUAL:
            self.write(f"mov [MEMORY + {start_index}], rax")
        elif operator == tokens.PLUS_EQUAL:
            self.write("xor r10, r10")
            self.write(f"mov r10, [MEMORY + {start_index}]")
            self.write(f"add r10, rax")
            self.write(f"mov [MEMORY + {start_index}], r10")
        elif operator == tokens.MINUS_EQUAL:
            self.write("xor r10, r10")
            self.write(f"mov r10, [MEMORY + {start_index}]")
            self.write(f"sub r10, rax")
            self.write(f"mov [MEMORY + {start_index}], r10")
        elif operator == tokens.STAR_EQUAL:
            self.write("xor r10, r10")
            self.write(f"mov r10, [MEMORY + {start_index}]")
            self.write(f"imul r10, rax")
            self.write(f"mov [MEMORY + {start_index}], r10")
        elif operator == tokens.SLASH_EQUAL:
            self.write("xor r10, r10")
            self.write(f"mov r10, [MEMORY + {start_index}]")
            self.write(f"idiv rax")
            self.write(f"mov [MEMORY + {start_index}], r10")
        # push end result
        self.write("push r10")
    
    def execute_block(self, block: BlockStmt, environment: Environment):
        prev = self.environment
        self.environment = environment
        for statement in block.statements:
            self.execute(statement)
        self.environment = prev

    # handles block statements
    def visit_block_stmt(self, block_stmt: BlockStmt):
        env = Environment()
        env.set_environment(self.environment)
        self.execute_block(block_stmt, env)
