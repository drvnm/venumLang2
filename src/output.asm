 section .text
   global main
 print:
   push    rbp
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
 main:
   push 0
   pop rax ; store variable SYSNONE
   mov [MEMORY + 40], rax
   xor rax, rax
   push 0
   pop rax ; store variable SYS_READ
   mov [MEMORY + 48], rax
   xor rax, rax
   push 1
   pop rax ; store variable SYS_WRITE
   mov [MEMORY + 56], rax
   xor rax, rax
   push 2
   pop rax ; store variable SYS_OPEN
   mov [MEMORY + 64], rax
   xor rax, rax
   push 3
   pop rax ; store variable SYS_CLOSE
   mov [MEMORY + 72], rax
   xor rax, rax
   push 0
   pop rax ; store variable STDIN
   mov [MEMORY + 80], rax
   xor rax, rax
   push 1
   pop rax ; store variable STDOUT
   mov [MEMORY + 88], rax
   xor rax, rax
   push 3
   pop rax ; store variable STDERR
   mov [MEMORY + 96], rax
   xor rax, rax
