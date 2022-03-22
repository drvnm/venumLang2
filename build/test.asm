section .text
   global _start

print:   push    rbp
   mov     rbp, rsp
   sub     rsp, 64
   mov     DWORD   [rbp-52], edi
   mov     DWORD   [rbp-4], 1
   mov     eax, DWORD   [rbp-4]
   movsx   rdx, eax
   mov     eax, 32
   sub     rax, rdx
   mov     BYTE   [rbp-48+rax], 10
.L2:
   mov     edx, DWORD   [rbp-52]
   movsx   rax, edx
   imul    rax, rax, 1717986919
   shr     rax, 32
   sar     eax, 2
   mov     esi, edx
   sar     esi, 31
   sub     eax, esi
   mov     ecx, eax
   mov     eax, ecx
   sal     eax, 2
   add     eax, ecx
   add     eax, eax
   mov     ecx, edx
   sub     ecx, eax
   mov     eax, ecx
   lea     ecx, [rax+48]
   mov     eax, DWORD   [rbp-4]
   movsx   rdx, eax
   mov     eax, 31
   sub     rax, rdx
   mov     edx, ecx
   mov     BYTE   [rbp-48+rax], dl
   add     DWORD   [rbp-4], 1
   mov     eax, DWORD   [rbp-52]
   movsx   rdx, eax
   imul    rdx, rdx, 1717986919
   shr     rdx, 32
   sar     edx, 2
   sar     eax, 31
   mov     ecx, eax
   mov     eax, edx
   sub     eax, ecx
   mov     DWORD   [rbp-52], eax
   cmp     DWORD   [rbp-52], 0
   jg      .L2
   mov     eax, DWORD   [rbp-4]
   cdqe
   mov     edx, DWORD   [rbp-4]
   movsx   rdx, edx
   mov     ecx, 32
   sub     rcx, rdx
   lea     rdx, [rbp-48]
   add     rcx, rdx
   mov     rdx, rax
   mov     rsi, rcx
   mov     edi, 1
   mov     rax, 1
   syscall
   nop
   leave
   ret
_start:
    ; push 5 onto stack
    push 5
    ; push 5 onto stack
    push 5
    ; checks if element is equal to
    pop rdi
    pop rax
    cmp rax, rdi
    sete al
    movzx rax, al
    push rax
    ; if statement
    pop rax
    cmp rax, 0
    je if_14
    ; push "5 == 5" onto stack
    mov rdx, 7
    push rdx
    push str_4
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; push 10 onto stack
    push 10
    ; push 20 onto stack
    push 20
    ; checks if element is equal to
    pop rdi
    pop rax
    cmp rax, rdi
    sete al
    movzx rax, al
    push rax
    ; if statement
    pop rax
    cmp rax, 0
    je if_13
    ; push "10 == 1" onto stack
    mov rdx, 8
    push rdx
    push str_10
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_13:    ; end statement
 if_14:    
    ; end of code, exit status
    mov rax, 60
    mov rdi, 0
    syscall

section .data
str_4:
    db 0x35, 0x20, 0x3d, 0x3d, 0x20, 0x35, 0xa
str_10:
    db 0x31, 0x30, 0x20, 0x3d, 0x3d, 0x20, 0x31, 0xa
