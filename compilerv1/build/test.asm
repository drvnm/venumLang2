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
    ; push "./home.html" onto stack
    push 11
    push str_91
    pop rsi
    pop rdi
    ; function call
    call str_to_pointer
    push rax
    pop rdi
    ; function call
    call open_file
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1008
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 1000 onto stack
    push 1000
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 8
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1008
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
    call read_file
    push rax
    ; calls print label to print top of stack
    pop rdi
    call print
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1008
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    pop rdi
    ; function call
    call close_file
    push rax
    ; push 2 onto stack
    push 2
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1016
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 14619 onto stack
    push 14619
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1018
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 0 onto stack
    push 0
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1020
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 0 onto stack
    push 0
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1024
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 0 onto stack
    push 0
    ; push 1 onto stack
    push 1
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1016
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
    mov rdi, 1028
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1028
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
    je if_137
    ; push "Couldnt create socket\n" onto stack
    push 22
    push str_132
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; push 1 onto stack
    push 1
    ; exit process
    mov rax, 60
    mov rdi, 0
    syscall
    ; else statement
    jmp if_143
 if_137:
    ; push "Socket created, is: " onto stack
    push 20
    push str_137
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
    mov rdi, 1028
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
 if_143:
 do_143:
    ; push 16 onto stack
    push 16
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1016
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1028
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
    je if_155
    ; push "Couldnt bind socket\n" onto stack
    push 20
    push str_151
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; exit process
    mov rax, 60
    mov rdi, 0
    syscall
    ; else statement
    jmp if_158
 if_155:
    ; push "Socket bound\n" onto stack
    push 13
    push str_155
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_158:
 do_158:
    ; push 5 onto stack
    push 5
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1028
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
    je if_169
    ; push "Couldnt listen to socket\n" onto stack
    push 25
    push str_165
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; exit process
    mov rax, 60
    mov rdi, 0
    syscall
    ; else statement
    jmp if_172
 if_169:
    ; push "Socket listening\n" onto stack
    push 17
    push str_169
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_172:
 do_172:
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1024
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1016
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1028
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
    mov rdi, 1036
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1036
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
    je if_188
    ; push "Couldnt accept connection\n" onto stack
    push 26
    push str_184
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; exit process
    mov rax, 60
    mov rdi, 0
    syscall
    ; else statement
    jmp if_196
 if_188:
    ; push "Connection accepted, is: " onto stack
    push 25
    push str_188
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
    mov rdi, 1036
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
    push str_193
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_196:
 do_196:
    ; push 1000 onto stack
    push 1000
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 8
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1036
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
    
    ; end of code, exit status
    mov rax, 60
    mov rdi, 0
    syscall
 ; function definition
    open_socket:
    push rbp
    mov rbp, rsp
    push rdi
    push rsi
    push rdx
    ; push 41 onto stack
    push 41
    pop rax
    pop rdi
    pop rsi
    pop rdx
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
    pop rax
    pop rdi
    pop rsi
    pop rdx
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
    pop rax
    pop rdi
    pop rsi
    pop rdx
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
    pop rax
    pop rdi
    pop rsi
    pop rdx
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
    pop rax
    pop rdi
    pop rsi
    pop rdx
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
    open_file:
    push rbp
    mov rbp, rsp
    push rdi
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 0 onto stack
    push 0
    ; push 0 onto stack
    push 0
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    ; push 2 onto stack
    push 2
    pop rax
    pop rdi
    pop rsi
    pop rdx
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
    read_file:
    push rbp
    mov rbp, rsp
    push rdi
    push rsi
    push rdx
    ; push 0 onto stack
    push 0
    pop rax
    pop rdi
    pop rsi
    pop rdx
    syscall
    push rax
    ; function end
    leave
    ret
; function definition
    close_file:
    push rbp
    mov rbp, rsp
    push rdi
    ; push 3 onto stack
    push 3
    pop rax
    pop rdi
    syscall
    push rax
    ; function end
    leave
    ret
; function definition
    str_to_pointer:
    push rbp
    mov rbp, rsp
    push rdi
    push rsi
    ; swaps top two elements on stack
    pop rdi
    pop rsi
    push rdi
    push rsi
    ; pops top of stack
    pop rax
    ; early return
    pop rax
    leave
    ret
    ; function end
    leave
    ret


section .data
str_91:
    db `./home.html`, 0
str_132:
    db `Couldnt create socket\n`, 0
str_137:
    db `Socket created, is: `, 0
str_151:
    db `Couldnt bind socket\n`, 0
str_155:
    db `Socket bound\n`, 0
str_165:
    db `Couldnt listen to socket\n`, 0
str_169:
    db `Socket listening\n`, 0
str_184:
    db `Couldnt accept connection\n`, 0
str_188:
    db `Connection accepted, is: `, 0
str_193:
    db `\n`, 0

section .bss
    ; MEMORY
  MEMORY: resb 64000
    ; heap
