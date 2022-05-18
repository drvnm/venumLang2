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
   push 2
   pop rax ; store variable AF_INET
   mov [MEMORY + 136], ax
   xor rax, rax
   push 45060
   pop rax ; store variable PORT
   mov [MEMORY + 138], ax
   xor rax, rax
   push 0
   pop rax ; store variable INADDR_ANY
   mov [MEMORY + 140], eax
   xor rax, rax
   push 1
   pop rax ; store variable SOCK_STREAM
   mov [MEMORY + 144], eax
   xor rax, rax
   push 1
   xor rax, rax
   pop rax ; store array initializer
   mov [(MEMORY + 148) + 0], al
   push 2
   xor rax, rax
   pop rax ; store array initializer
   mov [(MEMORY + 148) + 1], al
   push 3
   xor rax, rax
   pop rax ; store array initializer
   mov [(MEMORY + 148) + 2], al
   push 4
   xor rax, rax
   pop rax ; store array initializer
   mov [(MEMORY + 148) + 3], al
   push 5
   xor rax, rax
   pop rax ; store array initializer
   mov [(MEMORY + 148) + 4], al
   xor rax, rax ; begin loading from var
   mov ax, WORD [MEMORY + 136]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 144]
   push rax
   xor rsi, rsi
   pop rsi ; func call arg
   push 0
   xor rdx, rdx
   pop rdx ; func call arg
   call socket
   push rax
   xor rax, rax
   pop rax ; store variable sersock
   mov [MEMORY + 153], eax
   xor rax, rax
   push str_1
   xor rdi, rdi
   pop rdi ; func call arg
   call printstring
   push rax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 153]
   push rax
   pop rdi ; print statement
   call print
   push 0
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 153]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   mov rax, MEMORY + 136
   push rax
   xor rsi, rsi
   pop rsi ; func call arg
   push 16
   xor rdx, rdx
   pop rdx ; func call arg
   call bind
   push rax
   xor rax, rax
   pop rax ; compare left to right
   pop rbx
   cmp rax, rbx
   setl al
   movzx rax, al
   push rax
   pop rax ; if condition start
   cmp rax, 0
   je .L387
   push str_2
   xor rdi, rdi
   pop rdi ; func call arg
   call printline
   push rax
   xor rax, rax
   push 1
   xor rdi, rdi
   pop rdi ; func call arg
   call exit
   push rax
   xor rax, rax
   jmp .L387
 .L387: ; END IF STMT
   push 0
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 153]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   push 1
   xor rsi, rsi
   pop rsi ; func call arg
   call listen
   push rax
   xor rax, rax
   pop rax ; compare left to right
   pop rbx
   cmp rax, rbx
   setl al
   movzx rax, al
   push rax
   pop rax ; if condition start
   cmp rax, 0
   je .L410
   push str_3
   xor rdi, rdi
   pop rdi ; func call arg
   call printline
   push rax
   xor rax, rax
   push 1
   xor rdi, rdi
   pop rdi ; func call arg
   call exit
   push rax
   xor rax, rax
   jmp .L410
 .L410: ; END IF STMT
   push 0
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 153]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   mov rax, MEMORY + 136
   push rax
   xor rsi, rsi
   pop rsi ; func call arg
   push 16
   xor rdx, rdx
   pop rdx ; func call arg
   call accept
   push rax
   xor rax, rax
   pop rax ; compare left to right
   pop rbx
   cmp rax, rbx
   setl al
   movzx rax, al
   push rax
   pop rax ; if condition start
   cmp rax, 0
   je .L436
   push str_4
   xor rdi, rdi
   pop rdi ; func call arg
   call printline
   push rax
   xor rax, rax
   push 1
   xor rdi, rdi
   pop rdi ; func call arg
   call exit
   push rax
   xor rax, rax
   jmp .L436
 .L436: ; END IF STMT
   ; end of program
   mov rax, 60
   mov rdi, 0
   syscall
    strlen:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 0], rdi
   push 0
   pop rax ; store variable index
   mov [MEMORY + 8], eax
   xor rax, rax
   .L13: ; WHILE START
   push 0
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 0]
   push rax
   xor r10, r10
   xor r9, r9
   pop r9 ; array pointer
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 8]
   push rax
   xor rax, rax
   pop r10 ; array index
   mov al, [r9 + r10 * 1]
   push rax
   xor r10, r10
   pop rax ; compare left to right
   pop rbx
   cmp rax, rbx
   setg al
   movzx rax, al
   push rax
   pop rax ; while condition start
   cmp rax, 0
   je .L28
   push 1
   xor rax, rax ; assign value to variable
   pop rax
   xor r10, r10
   mov r10, [MEMORY + 8]
   add rax, r10
   mov [MEMORY + 8], DWORD eax
   jmp .L13
   .L28: ; WHILE END
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 8]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 printline:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 12], rdi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 12]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   call strlen
   push rax
   xor rax, rax
   pop rax ; store variable length
   mov [MEMORY + 20], eax
   xor rax, rax
   push 1
   pop rdi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 12]
   push rax
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 20]
   push rax
   pop rdx
   mov rax, 1
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 24], eax
   xor rax, rax
   push 1
   pop rdi
   push str_0
   pop rsi
   push 1
   pop rdx
   mov rax, 1
   syscall
   push rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 24]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 printstring:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 28], rdi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 28]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   call strlen
   push rax
   xor rax, rax
   pop rax ; store variable length
   mov [MEMORY + 36], eax
   xor rax, rax
   push 1
   pop rdi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 28]
   push rax
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 36]
   push rax
   pop rdx
   mov rax, 1
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 40], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 40]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 strcomp:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 44], rdi
   mov [MEMORY + 52], rsi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 44]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   call strlen
   push rax
   xor rax, rax
   pop rax ; store variable length1
   mov [MEMORY + 60], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 52]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   call strlen
   push rax
   xor rax, rax
   pop rax ; store variable length2
   mov [MEMORY + 64], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 64]
   push rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 60]
   push rax
   pop rax ; compare left to right
   pop rbx
   cmp rax, rbx
   setne al
   movzx rax, al
   push rax
   pop rax ; if condition start
   cmp rax, 0
   je .L140
   push 0
   pop rax ; return value
   leave
   ret
   jmp .L140
 .L140: ; END IF STMT
   push 0
   pop rax ; store variable i
   mov [MEMORY + 68], eax
   xor rax, rax
   .L141: ; WHILE START
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 60]
   push rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 68]
   push rax
   pop rax ; compare left to right
   pop rbx
   cmp rax, rbx
   setl al
   movzx rax, al
   push rax
   pop rax ; while condition start
   cmp rax, 0
   je .L174
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 52]
   push rax
   xor r10, r10
   xor r9, r9
   pop r9 ; array pointer
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 68]
   push rax
   xor rax, rax
   pop r10 ; array index
   mov al, [r9 + r10 * 1]
   push rax
   xor r10, r10
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 44]
   push rax
   xor r10, r10
   xor r9, r9
   pop r9 ; array pointer
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 68]
   push rax
   xor rax, rax
   pop r10 ; array index
   mov al, [r9 + r10 * 1]
   push rax
   xor r10, r10
   pop rax ; compare left to right
   pop rbx
   cmp rax, rbx
   setne al
   movzx rax, al
   push rax
   pop rax ; if condition start
   cmp rax, 0
   je .L173
   push 0
   pop rax ; return value
   leave
   ret
   jmp .L173
 .L173: ; END IF STMT
   push 1
   xor rax, rax ; assign value to variable
   pop rax
   xor r10, r10
   mov r10, [MEMORY + 68]
   add rax, r10
   mov [MEMORY + 68], DWORD eax
   jmp .L141
   .L174: ; WHILE END
   push 1
   pop rax ; return value
   leave
   ret
   leave
   ret
 socket:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 72], edi
   mov [MEMORY + 76], esi
   mov [MEMORY + 80], edx
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 72]
   push rax
   pop rdi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 76]
   push rax
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 80]
   push rax
   pop rdx
   mov rax, 41
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 84], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 84]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 bind:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 88], edi
   mov [MEMORY + 92], esi
   mov [MEMORY + 96], edx
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 88]
   push rax
   pop rdi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 92]
   push rax
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 96]
   push rax
   pop rdx
   mov rax, 49
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 100], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 100]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 listen:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 104], edi
   mov [MEMORY + 108], esi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 104]
   push rax
   pop rdi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 108]
   push rax
   pop rsi
   mov rax, 50
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 112], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 112]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 accept:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 116], edi
   mov [MEMORY + 120], esi
   mov [MEMORY + 124], edx
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 116]
   push rax
   pop rdi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 120]
   push rax
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 124]
   push rax
   pop rdx
   mov rax, 288
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 128], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 128]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 exit:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 132], edi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 132]
   push rax
   pop rdi
   mov rax, 60
   syscall
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret

 section .bss
   MEMORY: resb 64000
 section .data
   str_0: db `\n`, 0
   str_1: db `fd is: `, 0
   str_2: db `bind error`, 0
   str_3: db `listen error`, 0
   str_4: db `accept error`, 0
