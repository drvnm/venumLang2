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
    ; push 1 onto stack
    push 1
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 8
    add rax, rdi
    push rax
    ; push 0 onto stack
    push 0
    ; write bytes to array
    pop rdi
    pop rax
    pop rdx
    mov [rax + rdi * 1], rdx
    ; push 2 onto stack
    push 2
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 8
    add rax, rdi
    push rax
    ; push 1 onto stack
    push 1
    ; write bytes to array
    pop rdi
    pop rax
    pop rdx
    mov [rax + rdi * 1], rdx
    ; push 3 onto stack
    push 3
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 10
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 8
    add rax, rdi
    push rax
    ; push 0 onto stack
    push 0
    ; loads bytes from array
    pop rdi
    pop r10
    xor rax, rax
    mov AL, BYTE [r10 + rdi * 1]
    push rax
    ; calls print label to print top of stack
    pop rdi
    call print
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 8
    add rax, rdi
    push rax
    ; push 1 onto stack
    push 1
    ; loads bytes from array
    pop rdi
    pop r10
    xor rax, rax
    mov AL, BYTE [r10 + rdi * 1]
    push rax
    ; calls print label to print top of stack
    pop rdi
    call print
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 10
    add rax, rdi
    push rax
    ; load byte from variable
    pop r10
    xor rax, rax
    mov AL, BYTE [r10]
    push rax
    ; calls print label to print top of stack
    pop rdi
    call print
    ; push "./home.html" onto stack
    push 11
    push str_113
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
    mov rdi, 1011
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; push 100 onto stack
    push 100
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 11
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1011
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
    mov rdi, 1011
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
    mov rdi, 1019
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
    mov rdi, 1021
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
    mov rdi, 1023
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
    mov rdi, 1027
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
    mov rdi, 1019
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
    mov rdi, 1031
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1031
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
    je if_159
    ; push "Couldnt create socket\n" onto stack
    push 22
    push str_154
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
    jmp if_165
 if_159:
    ; push "Socket created, is: " onto stack
    push 20
    push str_159
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
    mov rdi, 1031
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
 if_165:
 do_165:
    ; push 16 onto stack
    push 16
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1019
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1031
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
    je if_177
    ; push "Couldnt bind socket\n" onto stack
    push 20
    push str_173
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
    jmp if_180
 if_177:
    ; push "Socket bound\n" onto stack
    push 13
    push str_177
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_180:
 do_180:
    ; push 5 onto stack
    push 5
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1031
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
    je if_191
    ; push "Couldnt listen to socket\n" onto stack
    push 25
    push str_187
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
    jmp if_194
 if_191:
    ; push "Socket listening\n" onto stack
    push 17
    push str_191
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_194:
 do_194:
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1027
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1019
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1031
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
    mov rdi, 1039
    add rax, rdi
    push rax
    ; writes byte to variable
    pop rax
    pop rdi
    mov [rax], rdi
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1039
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
    je if_210
    ; push "Couldnt accept connection\n" onto stack
    push 26
    push str_206
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
    jmp if_218
 if_210:
    ; push "Connection accepted, is: " onto stack
    push 25
    push str_210
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
    mov rdi, 1039
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
    push str_215
    ; calls syscall 1
    mov rax, 1
    mov rdi, 1
    pop r8
    pop r9
    mov rsi, r8
    mov rdx, r9
    syscall
    ; end statement
 if_218:
 do_218:
    ; push "HTTP/1.1 200 OK\n" onto stack
    push 16
    push str_218
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1039
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
    push str_222
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1039
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
    push str_226
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1039
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
    push str_230
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1039
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
    push str_234
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1039
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
    push str_238
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1039
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
    mov rdi, 11
    add rax, rdi
    push rax
    ; variable declaration
    mov rax, MEMORY
    mov rdi, 1039
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
str_113:
    db `./home.html`, 0
str_154:
    db `Couldnt create socket\n`, 0
str_159:
    db `Socket created, is: `, 0
str_173:
    db `Couldnt bind socket\n`, 0
str_177:
    db `Socket bound\n`, 0
str_187:
    db `Couldnt listen to socket\n`, 0
str_191:
    db `Socket listening\n`, 0
str_206:
    db `Couldnt accept connection\n`, 0
str_210:
    db `Connection accepted, is: `, 0
str_215:
    db `\n`, 0
str_218:
    db `HTTP/1.1 200 OK\n`, 0
str_222:
    db `Server: Atest\n`, 0
str_226:
    db `Content-Type: text/html\n`, 0
str_230:
    db `Connection: Closed\n`, 0
str_234:
    db `\n`, 0
str_238:
    db `<h1>Hello World!</h1>\n`, 0

section .bss
    ; MEMORY
  MEMORY: resb 64000
    ; heap
