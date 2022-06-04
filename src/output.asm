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
   push 2
   pop rax ; store variable AF_INET
   mov [MEMORY + 198], ax
   xor rax, rax
   push 16415
   pop rax ; store variable PORT
   mov [MEMORY + 200], ax
   xor rax, rax
   push 0
   pop rax ; store variable INADDR_ANY
   mov [MEMORY + 202], eax
   xor rax, rax
   push 1
   pop rax ; store variable SOCK_STREAM
   mov [MEMORY + 206], eax
   xor rax, rax
   push 16
   pop rax ; store variable length
   mov [MEMORY + 210], eax
   xor rax, rax
   mov rax, 0 ; store variable newsock
   mov [MEMORY + 214], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov ax, WORD [MEMORY + 198]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 206]
   push rax
   xor rsi, rsi
   pop rsi ; func call arg
   push 0
   xor rdx, rdx
   pop rdx ; func call arg
   xor rax, rax
   call socket
   push rax
   xor rax, rax
   pop rax ; store variable sersock
   mov [MEMORY + 218], eax
   xor rax, rax
   push str_1
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call printstring
   push rax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 218]
   push rax
   pop rdi ; print statement
   call print
   push 0
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 218]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   mov rax, MEMORY + 198
   push rax
   xor rsi, rsi
   pop rsi ; func call arg
   push 16
   xor rdx, rdx
   pop rdx ; func call arg
   xor rax, rax
   call bind
   push rax
   xor rax, rax
   pop rax ; left operand of binary op
   pop rbx ; right operand of binary op
   ; < rax, rbx
   cmp rax, rbx ; compare operation
   setl al
   movzx rax, al
   push rax
   pop rax ; if condition start
   cmp rax, 0
   je .L539
   push str_2
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call printline
   push rax
   xor rax, rax
   push 1
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call exit
   push rax
   xor rax, rax
   jmp .L539
 .L539: ; END IF STMT
   push 0
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 218]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   push 1
   xor rsi, rsi
   pop rsi ; func call arg
   xor rax, rax
   call listen
   push rax
   xor rax, rax
   pop rax ; left operand of binary op
   pop rbx ; right operand of binary op
   ; < rax, rbx
   cmp rax, rbx ; compare operation
   setl al
   movzx rax, al
   push rax
   pop rax ; if condition start
   cmp rax, 0
   je .L562
   push str_3
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call printline
   push rax
   xor rax, rax
   push 1
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call exit
   push rax
   xor rax, rax
   jmp .L562
 .L562: ; END IF STMT
   push 0
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 218]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   mov rax, MEMORY + 198
   push rax
   xor rsi, rsi
   pop rsi ; func call arg
   mov rax, MEMORY + 210
   push rax
   xor rdx, rdx
   pop rdx ; func call arg
   xor rax, rax
   call accept
   push rax
   xor rax, rax
   xor rax, rax ; assign value to variable
   pop rax
   mov [MEMORY + 214], eax
   push rax
   pop rax ; left operand of binary op
   pop rbx ; right operand of binary op
   ; < rax, rbx
   cmp rax, rbx ; compare operation
   setl al
   movzx rax, al
   push rax
   pop rax ; if condition start
   cmp rax, 0
   je .L593
   push str_4
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call printline
   push rax
   xor rax, rax
   push 1
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call exit
   push rax
   xor rax, rax
   jmp .L601
 .L593:
   push str_5
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call printline
   push rax
   xor rax, rax
 .L601: ; END IF STMT
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 214]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax ; begin loading from var
   mov rax, MEMORY + 222
   push rax
   xor rsi, rsi
   pop rsi ; func call arg
   push 1024
   xor rdx, rdx
   pop rdx ; func call arg
   xor rax, rax
   call read
   push rax
   xor rax, rax
   pop rax ; store variable result
   mov [MEMORY + 1246], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov rax, MEMORY + 222
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   push 32
   xor rsi, rsi
   pop rsi ; func call arg
   push 2
   xor rdx, rdx
   pop rdx ; func call arg
   xor rax, rax
   call chop_by_char
   push rax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov rax, MEMORY + 222
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call printline
   push rax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 214]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   push str_6
   xor rsi, rsi
   pop rsi ; func call arg
   xor rax, rax
   call send_to_client
   push rax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 214]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   push str_7
   xor rsi, rsi
   pop rsi ; func call arg
   xor rax, rax
   call send_to_client
   push rax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 214]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   push str_8
   xor rsi, rsi
   pop rsi ; func call arg
   xor rax, rax
   call send_to_client
   push rax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 214]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   push str_9
   xor rsi, rsi
   pop rsi ; func call arg
   xor rax, rax
   call send_to_client
   push rax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 214]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   push str_10
   xor rsi, rsi
   pop rsi ; func call arg
   xor rax, rax
   call send_to_client
   push rax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 214]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   push str_11
   xor rsi, rsi
   pop rsi ; func call arg
   xor rax, rax
   call send_to_client
   push rax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 214]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   push str_12
   xor rsi, rsi
   pop rsi ; func call arg
   xor rax, rax
   call send_to_client
   push rax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 218]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call close
   push rax
   xor rax, rax
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
   pop rax ; left operand of binary op
   pop rbx ; right operand of binary op
   ; > rax, rbx
   cmp rax, rbx ; compare operation
   setg al
   movzx rax, al
   push rax
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
   push rax
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
   xor rax, rax
   call strlen
   push rax
   xor rax, rax
   pop rax ; store variable length
   mov [MEMORY + 20], eax
   xor rax, rax
   push 1
   xor rdi, rdi
   pop rdi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 12]
   push rax
   xor rsi, rsi
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 20]
   push rax
   xor rdx, rdx
   pop rdx
   mov rax, 1
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 24], eax
   xor rax, rax
   push 1
   xor rdi, rdi
   pop rdi
   push str_0
   xor rsi, rsi
   pop rsi
   push 1
   xor rdx, rdx
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
   xor rax, rax
   call strlen
   push rax
   xor rax, rax
   pop rax ; store variable length
   mov [MEMORY + 36], eax
   xor rax, rax
   push 1
   xor rdi, rdi
   pop rdi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 28]
   push rax
   xor rsi, rsi
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 36]
   push rax
   xor rdx, rdx
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
   xor rax, rax
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
   xor rax, rax
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
   pop rax ; left operand of binary op
   pop rbx ; right operand of binary op
   ; != rax, rbx
   cmp rax, rbx ; compare operation
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
   pop rax ; left operand of binary op
   pop rbx ; right operand of binary op
   ; < rax, rbx
   cmp rax, rbx ; compare operation
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
   pop rax ; left operand of binary op
   pop rbx ; right operand of binary op
   ; != rax, rbx
   cmp rax, rbx ; compare operation
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
   push rax
   jmp .L141
   .L174: ; WHILE END
   push 1
   pop rax ; return value
   leave
   ret
   leave
   ret
 chop_by_char:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 72], rdi
   mov [MEMORY + 80], sil
   mov [MEMORY + 81], dl
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 72]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call strlen
   push rax
   xor rax, rax
   pop rax ; store variable length
   mov [MEMORY + 82], eax
   xor rax, rax
   push 0
   pop rax ; store variable i
   mov [MEMORY + 86], eax
   xor rax, rax
   .L203: ; WHILE START
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 82]
   push rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 86]
   push rax
   pop rax ; left operand of binary op
   pop rbx ; right operand of binary op
   ; < rax, rbx
   cmp rax, rbx ; compare operation
   setl al
   movzx rax, al
   push rax
   pop rax ; while condition start
   cmp rax, 0
   je .L254
   xor rax, rax ; begin loading from var
   mov al, BYTE [MEMORY + 80]
   push rax
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 72]
   push rax
   xor r10, r10
   xor r9, r9
   pop r9 ; array pointer
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 86]
   push rax
   xor rax, rax
   pop r10 ; array index
   mov al, [r9 + r10 * 1]
   push rax
   xor r10, r10
   pop rax ; left operand of binary op
   pop rbx ; right operand of binary op
   ; == rax, rbx
   cmp rax, rbx ; compare operation
   sete al
   movzx rax, al
   push rax
   pop rax ; if condition start
   cmp rax, 0
   je .L253
   push 1
   xor rax, rax ; begin loading from var
   mov al, BYTE [MEMORY + 81]
   push rax
   pop rax ; left operand of binary op
   pop rbx ; right operand of binary op
   ; - rax, rbx
   sub rax, rbx
   push rax
   xor rax, rax ; assign value to variable
   pop rax
   mov [MEMORY + 81], al
   push rax
   push 0
   xor rax, rax ; begin loading from var
   mov al, BYTE [MEMORY + 81]
   push rax
   pop rax ; left operand of binary op
   pop rbx ; right operand of binary op
   ; == rax, rbx
   cmp rax, rbx ; compare operation
   sete al
   movzx rax, al
   push rax
   pop rax ; if condition start
   cmp rax, 0
   je .L252
   push 0
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 86]
   push rax
   pop rax
   imul rax, 1
   mov rdi, QWORD [(MEMORY + 72)]
   add rdi, rax
   xor rax, rax
   pop rax
   mov [rdi], BYTE al
   push 1
   pop rax ; return value
   leave
   ret
   jmp .L252
 .L252: ; END IF STMT
   jmp .L253
 .L253: ; END IF STMT
   push 1
   xor rax, rax ; assign value to variable
   pop rax
   xor r10, r10
   mov r10, [MEMORY + 86]
   add rax, r10
   mov [MEMORY + 86], DWORD eax
   push rax
   jmp .L203
   .L254: ; WHILE END
   push 0
   pop rax ; return value
   leave
   ret
   leave
   ret
 socket:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 90], edi
   mov [MEMORY + 94], esi
   mov [MEMORY + 98], edx
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 90]
   push rax
   xor rdi, rdi
   pop rdi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 94]
   push rax
   xor rsi, rsi
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 98]
   push rax
   xor rdx, rdx
   pop rdx
   mov rax, 41
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 102], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 102]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 bind:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 106], edi
   mov [MEMORY + 110], esi
   mov [MEMORY + 114], edx
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 106]
   push rax
   xor rdi, rdi
   pop rdi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 110]
   push rax
   xor rsi, rsi
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 114]
   push rax
   xor rdx, rdx
   pop rdx
   mov rax, 49
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 118], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 118]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 listen:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 122], edi
   mov [MEMORY + 126], esi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 122]
   push rax
   xor rdi, rdi
   pop rdi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 126]
   push rax
   xor rsi, rsi
   pop rsi
   mov rax, 50
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 130], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 130]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 accept:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 134], edi
   mov [MEMORY + 138], esi
   mov [MEMORY + 142], edx
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 134]
   push rax
   xor rdi, rdi
   pop rdi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 138]
   push rax
   xor rsi, rsi
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 142]
   push rax
   xor rdx, rdx
   pop rdx
   mov rax, 43
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 146], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 146]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 exit:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 150], edi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 150]
   push rax
   xor rdi, rdi
   pop rdi
   mov rax, 60
   syscall
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 read:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 154], edi
   mov [MEMORY + 158], esi
   mov [MEMORY + 162], edx
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 154]
   push rax
   xor rdi, rdi
   pop rdi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 158]
   push rax
   xor rsi, rsi
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 162]
   push rax
   xor rdx, rdx
   pop rdx
   mov rax, 0
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 166], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 166]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 close:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 170], edi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 170]
   push rax
   xor rdi, rdi
   pop rdi
   mov rax, 6
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 174], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 174]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 send_to_client:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 178], edi
   mov [MEMORY + 182], rsi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 182]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call strlen
   push rax
   xor rax, rax
   pop rax ; store variable length
   mov [MEMORY + 190], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 178]
   push rax
   xor rdi, rdi
   pop rdi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 182]
   push rax
   xor rsi, rsi
   pop rsi
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 190]
   push rax
   xor rdx, rdx
   pop rdx
   mov rax, 1
   syscall
   push rax
   pop rax ; store variable result
   mov [MEMORY + 194], eax
   xor rax, rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 194]
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
   str_5: db `accepted`, 0
   str_6: db `HTTP/1.1 200 OK\r\n`, 0
   str_7: db `Server: Go-http-server\r\n`, 0
   str_8: db `Content-Length: 88\r\n`, 0
   str_9: db `Content-Type: text/html\r\n`, 0
   str_10: db `Connection: Closed\r\n`, 0
   str_11: db `\r\n`, 0
   str_12: db `<h1>Hello World!</h1>\r\n`, 0
