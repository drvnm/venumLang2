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
    ; push 0 onto stack
    push 0
    ; push "./home.html" onto stack
    push 11
    push str_4
    ; swaps top two elements on stack
    pop rdi
    pop rsi
    push rdi
    push rsi
    ; pops top of stack
    pop rax
    ; push 2 onto stack
    push 2
    pop rax
    pop rdi
    pop rsi
    pop rdx
    syscall
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1000
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1000
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
    ; push 100 onto stack
    push 100
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1000
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov RAX, QWORD [r10]
    push rax
    ; push 0 onto stack
    push 0
    pop rax
    pop rdi
    pop rsi
    pop rdx
    syscall
    push rax
    ; calls print label to print top of stack
    pop rdi
    call print
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1000
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
    ; push 2 onto stack
    push 2
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1008
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
    mov rdi, 1010
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
    mov rdi, 1012
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
    mov rdi, 1016
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
    mov rdi, 1008
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
    mov rdi, 1020
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1020
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
    je if_106
    ; push "Couldnt create socket\n" onto stack
    push 22
    push str_101
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
    jmp if_112
 if_106:
    ; push "Socket created, is: " onto stack
    push 20
    push str_106
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
    mov rdi, 1020
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
 if_112:
 do_112:
    ; push 16 onto stack
    push 16
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1008
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1020
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
    je if_124
    ; push "Couldnt bind socket\n" onto stack
    push 20
    push str_120
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
    jmp if_127
 if_124:
    ; push "Socket bound\n" onto stack
    push 13
    push str_124
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_127:
 do_127:
    ; push 5 onto stack
    push 5
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1020
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
    je if_138
    ; push "Couldnt listen to socket\n" onto stack
    push 25
    push str_134
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
    jmp if_141
 if_138:
    ; push "Socket listening\n" onto stack
    push 17
    push str_138
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_141:
 do_141:
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1016
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1008
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1020
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
    je if_157
    ; push "Couldnt accept connection\n" onto stack
    push 26
    push str_153
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
    jmp if_165
 if_157:
    ; push "Connection accepted, is: " onto stack
    push 25
    push str_157
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
    ; push "\n" onto stack
    push 1
    push str_162
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_165:
 do_165:
    ; push "HTTP/1.1 200 OK\n" onto stack
    push 16
    push str_165
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
    call fputs
    push rax
    ; push "Server: Atest\n" onto stack
    push 14
    push str_169
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
    call fputs
    push rax
    ; push "Content-Type: text/html\n" onto stack
    push 24
    push str_173
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
    call fputs
    push rax
    ; push "Connection: Closed\n" onto stack
    push 19
    push str_177
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
    call fputs
    push rax
    ; push "\n" onto stack
    push 1
    push str_181
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
    call fputs
    push rax
    ; push "<h1>Hello World!</h1>\n" onto stack
    push 22
    push str_185
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
    call fputs
    push rax
    ; push 100 onto stack
    push 100
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 0
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


section .data
str_4:
    db `./home.html`, 0
str_101:
    db `Couldnt create socket\n`, 0
str_106:
    db `Socket created, is: `, 0
str_120:
    db `Couldnt bind socket\n`, 0
str_124:
    db `Socket bound\n`, 0
str_134:
    db `Couldnt listen to socket\n`, 0
str_138:
    db `Socket listening\n`, 0
str_153:
    db `Couldnt accept connection\n`, 0
str_157:
    db `Connection accepted, is: `, 0
str_162:
    db `\n`, 0
str_165:
    db `HTTP/1.1 200 OK\n`, 0
str_169:
    db `Server: Atest\n`, 0
str_173:
    db `Content-Type: text/html\n`, 0
str_177:
    db `Connection: Closed\n`, 0
str_181:
    db `\n`, 0
str_185:
    db `<h1>Hello World!</h1>\n`, 0

section .bss
    ; MEMORY
  MEMORY: resb 64000
    ; heap
