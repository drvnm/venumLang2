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
    ; push 2 onto stack
    push 2
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 14619 onto stack
    push 14619
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 2
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 0 onto stack
    push 0
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 4
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 2 onto stack
    push 2
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 8
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 14619 onto stack
    push 14619
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 10
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 0 onto stack
    push 0
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 12
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 0 onto stack
    push 0
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 16
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 0 onto stack
    push 0
    ; function call
    call SOCK_STREAM
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov AX, WORD [r10]
    push rax
    pop rdx
    pop rsi
    pop rdi
    ; function call
    call open_socket
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 20
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 20
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    ; push 0 onto stack
    push 0
    ; checks if element is less then
    pop rdi
    pop rax
    cmp rax, rdi
    setl al
    movzx rax, al
    push rax
    ; if statement
    pop rax
    cmp rax, 0
    je if_101
    ; push "Couldnt create socket\n" onto stack
    push 22
    push str_98
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; else statement
    jmp if_107
 if_101:
    ; push "Socket created, is: " onto stack
    push 19
    push str_101
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 20
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    ; calls print label to print top of stack
    pop rdi
    call print
    ; end statement
 if_107:
 do_107:
    ; push 16 onto stack
    push 16
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 20
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    pop rdx
    pop rsi
    pop rdi
    ; function call
    call bind
    push rax
    ; push 0 onto stack
    push 0
    ; checks if element is not equal to
    pop rdi
    pop rax
    cmp rax, rdi
    setne al
    movzx rax, al
    push rax
    ; if statement
    pop rax
    cmp rax, 0
    je if_118
    ; push "Couldnt bind socket\n" onto stack
    push 20
    push str_115
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; else statement
    jmp if_121
 if_118:
    ; push "Socket bound\n" onto stack
    push 13
    push str_118
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_121:
 do_121:
    ; push 5 onto stack
    push 5
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 20
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    pop rsi
    pop rdi
    ; function call
    call listen
    push rax
    ; push 0 onto stack
    push 0
    ; checks if element is not equal to
    pop rdi
    pop rax
    cmp rax, rdi
    setne al
    movzx rax, al
    push rax
    ; if statement
    pop rax
    cmp rax, 0
    je if_131
    ; push "Couldnt listen to socket\n" onto stack
    push 25
    push str_128
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; else statement
    jmp if_134
 if_131:
    ; push "Socket listening\n" onto stack
    push 17
    push str_131
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_134:
 do_134:
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 16
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 8
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 20
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    pop rdx
    pop rsi
    pop rdi
    ; function call
    call accept
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 28
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 28
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    ; push 0 onto stack
    push 0
    ; checks if element is less then
    pop rdi
    pop rax
    cmp rax, rdi
    setl al
    movzx rax, al
    push rax
    ; if statement
    pop rax
    cmp rax, 0
    je if_149
    ; push "Couldnt accept connection\n" onto stack
    push 26
    push str_146
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; else statement
    jmp if_157
 if_149:
    ; push "Connection accepted, is: \n" onto stack
    push 26
    push str_149
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 28
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    ; calls print label to print top of stack
    pop rdi
    call print
    ; push "\n" onto stack
    push 1
    push str_154
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_157:
 do_157:
    ; while statement
 while_157:
    ; push 1 onto stack
    push 1
    ; do statement
    pop rax
    cmp rax, 0
    je do_179
    ; push 8 onto stack
    push 8
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 36
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 28
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    ; push 0 onto stack
    push 0
    pop r15
    mov rax, r15
    pop r15
    mov rdi, r15
    pop r15
    mov rsi, r15
    pop r15
    mov rdx, r15
    syscall
    push rax
    ; push "Message received: \n" onto stack
    push 19
    push str_166
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; push 8 onto stack
    push 8
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 36
    add rax, rdi
    push rax
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; push 0 onto stack
    push 0
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 36
    add rax, rdi
    push rax
    ; self.write byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push "Message has been sent!" onto stack
    push 21
    push str_174
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 28
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    pop rdx
    pop rsi
    pop rdi
    ; function call
    call fputs
    push rax
    ; jumps to while statement
    jmp while_157
    ; end statement
 if_179:
 do_179:
    
    ; end of code, exit status
    mov rax, 60
    mov rdi, 0
    syscall
 ; function definition
SOCK_STREAM:
    push rbp
    mov rbp, rsp
    ; push 1 onto stack
    push 1
    ; early return
    pop rax
    leave
    ret
    ; function end
    leave
    ret
; function definition
open_socket:
    push rbp
    mov rbp, rsp
    push rdi
    push rsi
    push rdx
    ; push 41 onto stack
    push 41
    pop r15
    mov rax, r15
    pop r15
    mov rdi, r15
    pop r15
    mov rsi, r15
    pop r15
    mov rdx, r15
    syscall
    push rax
    ; early return
    pop rax
    leave
    ret
    ; function end
    leave
    ret
; function definition
bind:
    push rbp
    mov rbp, rsp
    push rdi
    push rsi
    push rdx
    ; push 49 onto stack
    push 49
    pop r15
    mov rax, r15
    pop r15
    mov rdi, r15
    pop r15
    mov rsi, r15
    pop r15
    mov rdx, r15
    syscall
    push rax
    ; early return
    pop rax
    leave
    ret
    ; function end
    leave
    ret
; function definition
fputs:
    push rbp
    mov rbp, rsp
    push rdi
    push rsi
    push rdx
    ; push 1 onto stack
    push 1
    pop r15
    mov rax, r15
    pop r15
    mov rdi, r15
    pop r15
    mov rsi, r15
    pop r15
    mov rdx, r15
    syscall
    push rax
    ; early return
    pop rax
    leave
    ret
    ; function end
    leave
    ret
; function definition
listen:
    push rbp
    mov rbp, rsp
    push rdi
    push rsi
    ; push 50 onto stack
    push 50
    pop r15
    mov rax, r15
    pop r15
    mov rdi, r15
    pop r15
    mov rsi, r15
    pop r15
    mov rdx, r15
    syscall
    push rax
    ; early return
    pop rax
    leave
    ret
    ; function end
    leave
    ret
; function definition
accept:
    push rbp
    mov rbp, rsp
    push rdi
    push rsi
    push rdx
    ; push 43 onto stack
    push 43
    pop r15
    mov rax, r15
    pop r15
    mov rdi, r15
    pop r15
    mov rsi, r15
    pop r15
    mov rdx, r15
    syscall
    push rax
    ; early return
    pop rax
    leave
    ret
    ; function end
    leave
    ret


section .data
str_98:
    db 0x43, 0x6f, 0x75, 0x6c, 0x64, 0x6e, 0x74, 0x20, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x20, 0x73, 0x6f, 0x63, 0x6b, 0x65, 0x74, 0xa
str_101:
    db 0x53, 0x6f, 0x63, 0x6b, 0x65, 0x74, 0x20, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x2c, 0x20, 0x69, 0x73, 0x3a, 0x20
str_115:
    db 0x43, 0x6f, 0x75, 0x6c, 0x64, 0x6e, 0x74, 0x20, 0x62, 0x69, 0x6e, 0x64, 0x20, 0x73, 0x6f, 0x63, 0x6b, 0x65, 0x74, 0xa
str_118:
    db 0x53, 0x6f, 0x63, 0x6b, 0x65, 0x74, 0x20, 0x62, 0x6f, 0x75, 0x6e, 0x64, 0xa
str_128:
    db 0x43, 0x6f, 0x75, 0x6c, 0x64, 0x6e, 0x74, 0x20, 0x6c, 0x69, 0x73, 0x74, 0x65, 0x6e, 0x20, 0x74, 0x6f, 0x20, 0x73, 0x6f, 0x63, 0x6b, 0x65, 0x74, 0xa
str_131:
    db 0x53, 0x6f, 0x63, 0x6b, 0x65, 0x74, 0x20, 0x6c, 0x69, 0x73, 0x74, 0x65, 0x6e, 0x69, 0x6e, 0x67, 0xa
str_146:
    db 0x43, 0x6f, 0x75, 0x6c, 0x64, 0x6e, 0x74, 0x20, 0x61, 0x63, 0x63, 0x65, 0x70, 0x74, 0x20, 0x63, 0x6f, 0x6e, 0x6e, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0xa
str_149:
    db 0x43, 0x6f, 0x6e, 0x6e, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x20, 0x61, 0x63, 0x63, 0x65, 0x70, 0x74, 0x65, 0x64, 0x2c, 0x20, 0x69, 0x73, 0x3a, 0x20, 0xa
str_154:
    db 0xa
str_166:
    db 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x20, 0x72, 0x65, 0x63, 0x65, 0x69, 0x76, 0x65, 0x64, 0x3a, 0x20, 0xa
str_174:
    db 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x20, 0x68, 0x61, 0x73, 0x20, 0x62, 0x65, 0x65, 0x6e, 0x20, 0x73, 0x65, 0x6e, 0x74, 0x21

section .bss
    ; MEMORY
  MEMORY: resb 64000
    ; heap
