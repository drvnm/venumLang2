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
   push 1
   xor rax, rax
   pop rax ; store array initializer
   mov [(MEMORY + 10) + 0], rax
   push 2
   xor rax, rax
   pop rax ; store array initializer
   mov [(MEMORY + 10) + 1], rax
   xor rax, rax ; begin loading from var
   mov rax, MEMORY + 10
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   push 100
   xor rsi, rsi
   pop rsi ; func call arg
   call swap
   push 0
   pop rax ; store variable i
   mov [MEMORY + 0], eax
   .L59: ; WHILE START
   push 4
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 0]
   push rax
   pop rax ; compare left to right
   pop rbx
   cmp rax, rbx
   setl al
   movzx rax, al
   push rax
   pop rax ; while condition start
   cmp rax, 0
   je .L81
   xor rax, rax ; begin loading from var
   mov rax, MEMORY + 10
   push rax
   xor r9, r9
   pop r9 ; array pointer
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 0]
   push rax
   pop r10 ; array index
   xor rax, rax
   mov al, BYTE [r9 + r10 * 1]
   push rax
   pop rdi ; print statement
   call print
   push 1
   xor rax, rax ; assign value to variable
   pop rax
   xor r10, r10
   mov r10, [MEMORY + 0]
   add rax, r10
   mov [MEMORY + 0], DWORD eax
   push r10
   jmp .L59
   .L81: ; WHILE END
   ; end of program
   mov rax, 60
   mov rdi, 0
   syscall
    swap:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 0], rdi
   mov [MEMORY + 8], sil
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 0]
   push rax
   xor r9, r9
   pop r9 ; array pointer
   push 0
   pop r10 ; array index
   xor rax, rax
   mov al, BYTE [r9 + r10 * 1]
   push rax
   pop rax ; store variable temp
   mov [MEMORY + 9], al
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 0]
   push rax
   xor r9, r9
   pop r9 ; array pointer
   push 1
   pop r10 ; array index
   xor rax, rax
   mov al, BYTE [r9 + r10 * 1]
   push rax
   push 0
   pop rax
   imul rax, 1
   mov rdi, QWORD [(MEMORY + 0)]
   add rdi, rax
   xor rax, rax
   pop rax
   mov [rdi], BYTE al
   xor rax, rax ; begin loading from var
   mov al, BYTE [MEMORY + 9]
   push rax
   push 1
   pop rax
   imul rax, 1
   mov rdi, QWORD [(MEMORY + 0)]
   add rdi, rax
   xor rax, rax
   pop rax
   mov [rdi], BYTE al
   leave
   ret

 section .bss
   MEMORY: resb 6400
 section .data
