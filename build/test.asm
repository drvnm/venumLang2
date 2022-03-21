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
    ; push "hello, world!" onto stack
    mov rdx, 14
    push rdx
    push str_0
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    
    ; end of code, exit status
    mov rax, 60
    mov rdi, 0
    syscall

section .data
str_0:
    db 0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64, 0x21, 0xa
