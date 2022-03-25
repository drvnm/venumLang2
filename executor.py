from io import TextIOWrapper
from process import error
from typing import List
import subprocess
from tokens import tokens, Token

MEMORY_SIZE = 64_000


class Executor:
    def __init__(self, tokens: List[Token], path: str):
        self.path: str = path
        self.tokens: List[Token] = tokens
        self.file = open('./build/test.asm', 'w')
        self.subroutines: str = """ """
        self.append: bool = False

    def write(self, line: str):
        if self.append:
            self.subroutines += f"{line}\n"
        else:
            self.file.write(f"{line}\n")

    def execute(self):

        # self.write standard sections
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

        self.write("_start:")

        instruction = 0
        strings = []
        last_function = 0
        functions = {}
        while instruction < len(self.tokens):
            curr_instruction = self.tokens[instruction]
            if curr_instruction.type == tokens.PRINT:
                self.write(
                    f"    ; calls print label to print top of stack")
                self.write(f"    pop rdi")
                self.write(f"    call print")
                instruction += 1
            elif curr_instruction.type == tokens.PUTS:
                self.write(f"    ; calls syscall 1")
                self.write(f"    mov rax, 1")  # sycall number
                self.write(f"    mov rdi, 1")  # file descriptor
                self.write(f"    pop r8")  # string pointer
                self.write(f"    pop r9")  # length of string
                self.write(f"    mov rsi, r8")
                self.write(f"    mov rdx, r9")
                self.write(f"    syscall")

                # make self.write syscall
                instruction += 1

            elif curr_instruction.type == tokens.FLOAT_PUSH:
                self.write(
                    f"    ; push {curr_instruction.value} onto stack")
                self.write(f"    push {curr_instruction.value}")
                instruction += 1

            elif curr_instruction.type == tokens.INT_PUSH:
                self.write(
                    f"    ; push {curr_instruction.value} onto stack")
                self.write(f"    push {curr_instruction.value}")
                instruction += 1

            elif curr_instruction.type == tokens.STRING_PUSH:
                str_len = len(curr_instruction.value) + 1
                self.write(
                    f"    ; push \"{curr_instruction.value}\" onto stack")
                self.write(f"    mov rdx, {str_len}")
                self.write(f"    push rdx")
                self.write(f"    push str_{instruction}")
                strings.append((curr_instruction.value, instruction))
                instruction += 1

            # operators
            elif curr_instruction.type == tokens.PLUS:
                self.write(f"    ; add top two values on stack")
                self.write(f"    pop rdi")
                self.write(f"    pop rax")
                self.write(f"    add rax, rdi")
                self.write(f"    push rax")
                instruction += 1
            elif curr_instruction.type == tokens.MIN:
                self.write(f"    ; subtract top two values on stack")
                self.write(f"    pop rdi")
                self.write(f"    pop rax")
                self.write(f"    sub rax, rdi")
                self.write(f"    push rax")
                instruction += 1
            elif curr_instruction.type == tokens.MUL:
                self.write(f"    ; multiply top two values on stack")
                self.write(f"    pop rdi")
                self.write(f"    pop rax")
                self.write(f"    imul rax, rdi")
                self.write(f"    push rax")
                instruction += 1
            elif curr_instruction.type == tokens.DIV:
                self.write(f"    ; divide top two values on stack")
                self.write(f"    pop rdi")
                self.write(f"    pop rax")
                self.write(f"    cqo")
                self.write(f"    idiv rdi")
                self.write(f"    push rax")
                instruction += 1
            elif curr_instruction.type == tokens.GT:
                self.write(f"    ; checks if element is greater then")
                self.write(f"    pop rdi")
                self.write(f"    pop rax")
                self.write(f"    cmp rax, rdi")
                self.write(f"    setg al")
                self.write(f"    movzx rax, al")
                self.write(f"    push rax")
                instruction += 1
            elif curr_instruction.type == tokens.LT:
                self.write(f"    ; checks if element is less then")
                self.write(f"    pop rdi")
                self.write(f"    pop rax")
                self.write(f"    cmp rax, rdi")
                self.write(f"    setl al")
                self.write(f"    movzx rax, al")
                self.write(f"    push rax")
                instruction += 1
            elif curr_instruction.type == tokens.GTE:
                self.write(
                    f"    ; checks if element is greater then or equal to")
                self.write(f"    pop rdi")
                self.write(f"    pop rax")
                self.write(f"    cmp rax, rdi")
                self.write(f"    setge al")
                self.write(f"    movzx rax, al")
                self.write(f"    push rax")
                instruction += 1
            elif curr_instruction.type == tokens.LTE:
                self.write(
                    f"    ; checks if element is less then or equal to")
                self.write(f"    pop rdi")
                self.write(f"    pop rax")
                self.write(f"    cmp rax, rdi")
                self.write(f"    setle al")
                self.write(f"    movzx rax, al")
                self.write(f"    push rax")
                instruction += 1
            elif curr_instruction.type == tokens.EQ:
                self.write(f"    ; checks if element is equal to")
                self.write(f"    pop rdi")
                self.write(f"    pop rax")
                self.write(f"    cmp rax, rdi")
                self.write(f"    sete al")
                self.write(f"    movzx rax, al")
                self.write(f"    push rax")
                instruction += 1
            elif curr_instruction.type == tokens.NEQ:
                self.write(f"    ; checks if element is not equal to")
                self.write(f"    pop rdi")
                self.write(f"    pop rax")
                self.write(f"    cmp rax, rdi")
                self.write(f"    setne al")
                self.write(f"    movzx rax, al")
                self.write(f"    push rax")
                instruction += 1
            elif curr_instruction.type == tokens.COPY:
                self.write(f"    ; copies top value on stack")
                self.write(f"    pop rax")
                self.write(f"    push rax")
                self.write(f"    push rax")
                instruction += 1
            elif curr_instruction.type == tokens.MOD:
                self.write(f"    ; modulo top two values on stack")
                self.write(f"    pop rdi")
                self.write(f"    pop rax")
                self.write(f"    cqo")
                self.write(f"    idiv rdi")
                self.write(f"    push rdx")
                instruction += 1

            # branching
            elif curr_instruction.type == tokens.IFF:
                if not hasattr(curr_instruction, "jump"):
                    error("if statement was not closed",
                          curr_instruction.line, self.path, curr_instruction.col)
                self.write(f"    ; if statement")
                self.write(f"    pop rax")
                self.write(f"    cmp rax, 0")
                self.write(f"    je if_{curr_instruction.jump}")
                instruction += 1
            elif curr_instruction.type == tokens.END:
                if hasattr(curr_instruction, "jump"):
                    self.write(f"    ; jumps to while statement")
                    self.write(
                        f"    jmp while_{curr_instruction.jump}")
                self.write(f"    ; end statement")
                self.write(f" if_{instruction + 1}:")
                self.write(f" do_{instruction + 1}:")
                instruction += 1
            elif curr_instruction.type == tokens.ELSEF:
                after_end = curr_instruction.jump
                self.write(f"    ; else statement")
                self.write(f"    jmp if_{after_end}")
                self.write(f" if_{instruction + 1}:")
                instruction += 1
            elif curr_instruction.type == tokens.DO:
                end_ip = curr_instruction.jump
                self.write(f"    ; do statement")
                self.write(f"    pop rax")
                self.write(f"    cmp rax, 0")
                self.write(f"    je do_{end_ip}")
                instruction += 1

            elif curr_instruction.type == tokens.WHILEF:
                self.write(f"    ; while statement")
                self.write(f" while_{instruction}:")
                instruction += 1

            # variables
            elif curr_instruction.type == tokens.IDENTIFIER:
                adress = curr_instruction.size
                self.write(f"    ; variable declaration")
                self.write(f"    mov rax, MEMORY")
                self.write(f"    mov rdi, {adress}")
                self.write(f"    add rax, rdi")
                self.write(f"    push rax")
                instruction += 1

            # Writes a byte to a variable
            elif curr_instruction.type == tokens.WRITE:
                self.write(f"    ; self.write byte to variable")
                self.write(f"    pop rax")
                self.write(f"    pop rdi")
                self.write(f"    mov [rax], rdi")
                instruction += 1
            # LOAD a byte from a variable
            elif curr_instruction.type == tokens.LOAD:
                self.write(f"    ; load byte from variable")
                self.write(f"    pop rax")
                self.write(f"    xor rbx, rbx")
                self.write(f"    mov rbx, qword [rax]")
                self.write(f"    push rbx")
                instruction += 1
            elif curr_instruction.type == tokens.FUNC:
                self.append = True
                self.write(f"    ; function def")
                self.write(f"  {curr_instruction.name}:")
                self.write(f"    push rbp")
                self.write(f"    mov rbp, rsp")
                instruction += 1
            elif curr_instruction.type == tokens.FUNC_END:
                self.write(f"    ; function end")
                self.write(f"    leave")
                self.write(f"    ret")
                instruction += 1
                self.append = False
            elif curr_instruction.type == tokens.FUNC_CALL:
                self.write(f"    ; function call")
                self.write(f"    call {curr_instruction.value}")
                instruction += 1

            else:
                instruction += 1
        # exit
        self.write("    ")
        self.write("    ; end of code, exit status")
        self.write("    mov rax, 60")
        self.write("    mov rdi, 0")
        self.write("    syscall")
    
        # writes subroutine buffer to file
        self.file.write(self.subroutines)

        # .data section for literals
        self.write("")
        self.write("section .data")
        for string, index in strings:
            byte_str = bytes(string, "utf-8").decode("unicode_escape")
            str_hex = "db " + \
                ", ".join(
                    map(hex, list(bytearray(byte_str, encoding="utf-8")) + [10]))
            self.write(f"str_{index}:")
            self.write(f"    {str_hex}")

        # .bss
        self.write(f"")
        self.write(f"section .bss")
        self.write(f"    ; MEMORY")
        self.write(f"  MEMORY: resb {MEMORY_SIZE}")
        self.write(f"    ; heap")
        self.file.close()

        # compile and link
        subprocess.run(["nasm", "-f", "elf64", "./build/test.asm"])
        subprocess.run(["ld", "-o", "./build/test", "./build/test.o"])
