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
    ; push 0 onto stack
    push 0
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; while statement
 while_4:
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; load byte from variable
    pop rax
    xor rbx, rbx
    mov rbx, qword [rax]
    push rbx
    ; push 100 onto stack
    push 100
    ; checks if element is less then
    pop rdi
    pop rax
    cmp rax, rdi
    setl al
    movzx rax, al
    push rax
    ; do statement
    pop rax
    cmp rax, 0
    je do_56
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; load byte from variable
    pop rax
    xor rbx, rbx
    mov rbx, qword [rax]
    push rbx
    ; push 3 onto stack
    push 3
    ; modulo top two values on stack
    pop rdi
    pop rax
    cqo
    idiv rdi
    push rdx
    ; push 0 onto stack
    push 0
    ; checks if element is equal to
    pop rdi
    pop rax
    cmp rax, rdi
    sete al
    movzx rax, al
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; load byte from variable
    pop rax
    xor rbx, rbx
    mov rbx, qword [rax]
    push rbx
    ; push 5 onto stack
    push 5
    ; modulo top two values on stack
    pop rdi
    pop rax
    cqo
    idiv rdi
    push rdx
    ; push 0 onto stack
    push 0
    ; checks if element is equal to
    pop rdi
    pop rax
    cmp rax, rdi
    sete al
    movzx rax, al
    push rax
    ; double and
    pop rdi
    pop rax
    cmp rax, 1
    sete al
    cmp rdi, 1
    sete bl
    and al, bl
    movzx rax, al
    push rax
    ; if statement
    pop rax
    cmp rax, 0
    je if_27
    ; push "fizzbuzz" onto stack
    mov rdx, 9
    push rdx
    push str_24
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; else statement
    jmp if_49
 if_27:
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; load byte from variable
    pop rax
    xor rbx, rbx
    mov rbx, qword [rax]
    push rbx
    ; push 3 onto stack
    push 3
    ; modulo top two values on stack
    pop rdi
    pop rax
    cqo
    idiv rdi
    push rdx
    ; push 0 onto stack
    push 0
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
    je if_37
    ; push "fizz" onto stack
    mov rdx, 5
    push rdx
    push str_34
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; else statement
    jmp if_48
 if_37:
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; load byte from variable
    pop rax
    xor rbx, rbx
    mov rbx, qword [rax]
    push rbx
    ; push 5 onto stack
    push 5
    ; modulo top two values on stack
    pop rdi
    pop rax
    cqo
    idiv rdi
    push rdx
    ; push 0 onto stack
    push 0
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
    je if_47
    ; push "buzz" onto stack
    mov rdx, 5
    push rdx
    push str_44
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_47:
 do_47:
    ; end statement
 if_48:
 do_48:
    ; end statement
 if_49:
 do_49:
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; load byte from variable
    pop rax
    xor rbx, rbx
    mov rbx, qword [rax]
    push rbx
    ; push 1 onto stack
    push 1
    ; add top two values on stack
    pop rdi
    pop rax
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; jumps to while statement
    jmp while_4
    ; end statement
 if_56:
 do_56:
    
    ; end of code, exit status
    mov rax, 60
    mov rdi, 0
    syscall
 

section .data
str_24:
    db 0x66, 0x69, 0x7a, 0x7a, 0x62, 0x75, 0x7a, 0x7a, 0xa
str_34:
    db 0x66, 0x69, 0x7a, 0x7a, 0xa
str_44:
    db 0x62, 0x75, 0x7a, 0x7a, 0xa

section .bss
    ; MEMORY
  MEMORY: resb 64000
    ; heap
