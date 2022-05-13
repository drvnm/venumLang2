 section .text
   global _start
   section .text
      global _start
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
 _start:
   push 0
   pop rax ; store variable x
   mov [MEMORY + 0], rax
   .L0: ; WHILE START
   push 100
   xor rax, rax
   mov AL, BYTE [MEMORY + 0]
   push rax
   pop rax ; compare left to right
   pop rbx
   cmp rax, rbx
   setle al
   movzx rax, al
   push rax
   pop rax ; while condition start
   cmp rax, 0
   je .L18
   xor rax, rax
   mov AL, BYTE [MEMORY + 0]
   push rax
   pop rdi ; print statement
   call print
   push 1
   xor rax, rax ; assign value to variable x
   pop rax
   xor r10, r10
   mov r10, [MEMORY + 0]
   add r10, rax
   mov [MEMORY + 0], r10
   push r10
   jmp .L0
   .L18: ; WHILE END
   ; end of program
   mov rax, 60
   mov rdi, 0
   syscall
 section .bss
   MEMORY: resb 6400
