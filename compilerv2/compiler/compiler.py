import subprocess
from typing import List
from visitors.visitor import Visitor
from parsing.statements import *
from parsing.expressions import *
from intermediate.tokens import *


class Compiler(Visitor):
    def __init__(self):
        self.file = open("output.asm", "w")
        self.output_file = "output"

    # writes line to asm file
    def write(self, line: str, indent: int = True):
        print("attempt to write")
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

    def compile(self, expr: Expr):
        self.write_header()
        expr.accept(self)
        self.write("pop rdi")
        self.write("call print")
        self.write_footer()
        self.file.close()

        # compile and link
        subprocess.run(["nasm", "-f", "elf64", f"{self.output_file}.asm"])
        subprocess.run(
            ["ld", "-o", f"{self.output_file}", f"{self.output_file}.o"])

    def execute(self, expr: Expr):
        expr.accept(self)

    def visit_literal_expr(self, expr: LiteralExpr):
        literal = expr.value.literal if isinstance(expr.value, Token) else expr.value
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
            self.write(f"not rax")
            self.write(f"push rax")

    def visit_grouping_expr(self, grouping_expr: GroupingExpr):
        self.execute(grouping_expr.expr)

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
            self.write(f"pushf")
            print("yeaah")

