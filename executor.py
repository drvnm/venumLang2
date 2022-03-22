from process import error
from typing import List
import subprocess
from tokens import tokens, Token

class Executor:
    def __init__(self, tokens: List[Token], path: str):
        self.path: str = path
        self.tokens: List[Token] = tokens

    def execute(self):
        with open("./build/test.asm", 'w') as output:
            # write standard sections
            output.write("section .text\n")
            output.write("   global _start\n\n")
            
            output.write("print:")
            output.write("   push    rbp\n")
            output.write("   mov     rbp, rsp\n")
            output.write("   sub     rsp, 64\n")
            output.write("   mov     DWORD   [rbp-52], edi\n")
            output.write("   mov     DWORD   [rbp-4], 1\n")
            output.write("   mov     eax, DWORD   [rbp-4]\n")
            output.write("   movsx   rdx, eax\n")
            output.write("   mov     eax, 32\n")
            output.write("   sub     rax, rdx\n")
            output.write("   mov     BYTE   [rbp-48+rax], 10\n")
            output.write(".L2:\n")
            output.write("   mov     edx, DWORD   [rbp-52]\n")
            output.write("   movsx   rax, edx\n")
            output.write("   imul    rax, rax, 1717986919\n")
            output.write("   shr     rax, 32\n")
            output.write("   sar     eax, 2\n")
            output.write("   mov     esi, edx\n")
            output.write("   sar     esi, 31\n")
            output.write("   sub     eax, esi\n")
            output.write("   mov     ecx, eax\n")
            output.write("   mov     eax, ecx\n")
            output.write("   sal     eax, 2\n")
            output.write("   add     eax, ecx\n")
            output.write("   add     eax, eax\n")
            output.write("   mov     ecx, edx\n")
            output.write("   sub     ecx, eax\n")
            output.write("   mov     eax, ecx\n")
            output.write("   lea     ecx, [rax+48]\n")
            output.write("   mov     eax, DWORD   [rbp-4]\n")
            output.write("   movsx   rdx, eax\n")
            output.write("   mov     eax, 31\n")
            output.write("   sub     rax, rdx\n")
            output.write("   mov     edx, ecx\n")
            output.write("   mov     BYTE   [rbp-48+rax], dl\n")
            output.write("   add     DWORD   [rbp-4], 1\n")
            output.write("   mov     eax, DWORD   [rbp-52]\n")
            output.write("   movsx   rdx, eax\n")
            output.write("   imul    rdx, rdx, 1717986919\n")
            output.write("   shr     rdx, 32\n")
            output.write("   sar     edx, 2\n")
            output.write("   sar     eax, 31\n")
            output.write("   mov     ecx, eax\n")
            output.write("   mov     eax, edx\n")
            output.write("   sub     eax, ecx\n")
            output.write("   mov     DWORD   [rbp-52], eax\n")
            output.write("   cmp     DWORD   [rbp-52], 0\n")
            output.write("   jg      .L2\n")
            output.write("   mov     eax, DWORD   [rbp-4]\n")
            output.write("   cdqe\n")
            output.write("   mov     edx, DWORD   [rbp-4]\n")
            output.write("   movsx   rdx, edx\n")
            output.write("   mov     ecx, 32\n")
            output.write("   sub     rcx, rdx\n")
            output.write("   lea     rdx, [rbp-48]\n")
            output.write("   add     rcx, rdx\n")
            output.write("   mov     rdx, rax\n")
            output.write("   mov     rsi, rcx\n")
            output.write("   mov     edi, 1\n")
            output.write("   mov     rax, 1\n")
            output.write("   syscall\n")
            output.write("   nop\n")
            output.write("   leave\n")
            output.write("   ret\n")

            output.write("_start:\n")

            instruction = 0
            strings = []
            while instruction < len(self.tokens):
                curr_instruction = self.tokens[instruction]
                if curr_instruction.type == tokens.PRINT:
                    output.write(f"    ; calls print label to print top of stack\n")
                    output.write(f"    pop rdi\n")
                    output.write(f"    call print\n")
                    instruction += 1
                elif curr_instruction.type == tokens.PUTS:
                    output.write(f"    ; calls syscall 1\n")
                    output.write(f"    mov rax, 1\n") # sycall number
                    output.write(f"    mov rdi, 1\n") # file descriptor
                    output.write(f"    pop r8\n") # string pointer
                    output.write(f"    pop r9\n") # length of string
                    output.write(f"    mov rsi, r8\n")
                    output.write(f"    mov rdx, r9\n")
                    output.write(f"    syscall\n")

                    # make write syscall
                    instruction += 1

                elif curr_instruction.type == tokens.INT:
                    output.write(f"    ; push {curr_instruction.value} onto stack\n")
                    output.write(f"    push {curr_instruction.value}\n")
                    instruction += 1

                elif curr_instruction.type == tokens.FLOAT:
                    output.write(f"    ; push {curr_instruction.value} onto stack\n")
                    output.write(f"    push {curr_instruction.value}\n")
                    instruction += 1
                
                elif curr_instruction.type == tokens.STRING:
                    str_len = len(curr_instruction.value) + 1
                    output.write(f"    ; push \"{curr_instruction.value}\" onto stack\n")
                    output.write(f"    mov rdx, {str_len}\n")
                    output.write(f"    push rdx\n")
                    output.write(f"    push str_{instruction}\n")
                    strings.append((curr_instruction.value, instruction))
                    instruction += 1
                
                # operators
                elif curr_instruction.type == tokens.PLUS:
                    output.write(f"    ; add top two values on stack\n")
                    output.write(f"    pop rdi\n")
                    output.write(f"    pop rax\n")
                    output.write(f"    add rax, rdi\n")
                    output.write(f"    push rax\n")
                    instruction += 1
                elif curr_instruction.type == tokens.MIN:
                    output.write(f"    ; subtract top two values on stack\n")
                    output.write(f"    pop rdi\n")
                    output.write(f"    pop rax\n")
                    output.write(f"    sub rax, rdi\n")
                    output.write(f"    push rax\n")
                    instruction += 1
                elif curr_instruction.type == tokens.MUL:
                    output.write(f"    ; multiply top two values on stack\n")
                    output.write(f"    pop rdi\n")
                    output.write(f"    pop rax\n")
                    output.write(f"    imul rax, rdi\n")
                    output.write(f"    push rax\n")
                    instruction += 1
                elif curr_instruction.type == tokens.DIV:
                    output.write(f"    ; divide top two values on stack\n")
                    output.write(f"    pop rdi\n")
                    output.write(f"    pop rax\n")
                    output.write(f"    cqo\n")
                    output.write(f"    idiv rdi\n")
                    output.write(f"    push rax\n")
                    instruction += 1
                elif curr_instruction.type == tokens.GT:
                    output.write(f"    ; checks if element is greater then\n")
                    output.write(f"    pop rdi\n")
                    output.write(f"    pop rax\n")
                    output.write(f"    cmp rax, rdi\n")
                    output.write(f"    setg al\n")
                    output.write(f"    movzx rax, al\n")
                    output.write(f"    push rax\n")
                    instruction += 1
                elif curr_instruction.type == tokens.LT:
                    output.write(f"    ; checks if element is less then\n")
                    output.write(f"    pop rdi\n")
                    output.write(f"    pop rax\n")
                    output.write(f"    cmp rax, rdi\n")
                    output.write(f"    setl al\n")
                    output.write(f"    movzx rax, al\n")
                    output.write(f"    push rax\n")
                    instruction += 1
                elif curr_instruction.type == tokens.GTE:
                    output.write(f"    ; checks if element is greater then or equal to\n")
                    output.write(f"    pop rdi\n")
                    output.write(f"    pop rax\n")
                    output.write(f"    cmp rax, rdi\n")
                    output.write(f"    setge al\n")
                    output.write(f"    movzx rax, al\n")
                    output.write(f"    push rax\n")
                    instruction += 1
                elif curr_instruction.type == tokens.LTE:
                    output.write(f"    ; checks if element is less then or equal to\n")
                    output.write(f"    pop rdi\n")
                    output.write(f"    pop rax\n")
                    output.write(f"    cmp rax, rdi\n")
                    output.write(f"    setle al\n")
                    output.write(f"    movzx rax, al\n")
                    output.write(f"    push rax\n")
                    instruction += 1
                elif curr_instruction.type == tokens.EQ:
                    output.write(f"    ; checks if element is equal to\n")
                    output.write(f"    pop rdi\n")
                    output.write(f"    pop rax\n")
                    output.write(f"    cmp rax, rdi\n")
                    output.write(f"    sete al\n")
                    output.write(f"    movzx rax, al\n")
                    output.write(f"    push rax\n")
                    instruction += 1
                
                # branching
                elif curr_instruction.type == tokens.IFF:
                    if not hasattr(curr_instruction, "jump"):
                        error("if statement was not closed", curr_instruction.line, self.path, curr_instruction.col)
                    output.write(f"    ; if statement\n")
                    output.write(f"    pop rax\n")
                    output.write(f"    cmp rax, 0\n")
                    output.write(f"    je if_{curr_instruction.jump + 1}\n")
                    instruction += 1
                elif curr_instruction.type == tokens.END:
                    output.write(f"    ; end statement\n")
                    output.write(f" if_{instruction + 1}:")
                    instruction += 1

                else:
                    instruction += 1
            # exit
            output.write("    \n")
            output.write("    ; end of code, exit status\n")
            output.write("    mov rax, 60\n")
            output.write("    mov rdi, 0\n")
            output.write("    syscall\n")   

            # .data section for literals
            output.write("\n")
            output.write("section .data\n")
            for string, index in strings:
                byte_str = bytes(string, "utf-8").decode("unicode_escape")
                str_hex = "db " + ", ".join(map(hex, list(bytearray(byte_str, encoding="utf-8")) + [10] ))
                output.write(f"str_{index}:\n")
                output.write(f"    {str_hex}\n")

        # compile and link
        subprocess.run(["nasm", "-f", "elf64", "./build/test.asm"])
        subprocess.run(["ld", "-o", "./build/test", "./build/test.o"])

            
            
                
                
                    