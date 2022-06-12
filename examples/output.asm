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
   push 420
   pop rax ; negate top of stack
   neg rax
   push rax
   pop rax ; negate top of stack
   neg rax
   push rax
   pop rax ; negate top of stack
   neg rax
   push rax
   pop rax ; store variable foo
   mov [MEMORY + 165], eax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 165]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call printint
   push rax
   push str_2
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call println
   push rax
   xor rax, rax
   call return_to_sender
   push rax
   pop rax ; assign value to variable
   mov [MEMORY + 165], eax
   push rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 165]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call printint
   push rax
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
   pop rax ; assign value to variable
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
 strcomp:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 12], rdi
   mov [MEMORY + 20], rsi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 12]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call strlen
   push rax
   pop rax ; store variable length1
   mov [MEMORY + 28], eax
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 20]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call strlen
   push rax
   pop rax ; store variable length2
   mov [MEMORY + 32], eax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 32]
   push rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 28]
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
   je .L70
   push 0
   pop rax ; return value
   leave
   ret
   jmp .L70
 .L70: ; END IF STMT
   push 0
   pop rax ; store variable i
   mov [MEMORY + 36], eax
   .L71: ; WHILE START
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 28]
   push rax
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 36]
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
   je .L104
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 20]
   push rax
   xor r10, r10
   xor r9, r9
   pop r9 ; array pointer
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 36]
   push rax
   xor rax, rax
   pop r10 ; array index
   mov al, [r9 + r10 * 1]
   push rax
   xor r10, r10
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 12]
   push rax
   xor r10, r10
   xor r9, r9
   pop r9 ; array pointer
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 36]
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
   je .L103
   push 0
   pop rax ; return value
   leave
   ret
   jmp .L103
 .L103: ; END IF STMT
   push 1
   pop rax ; assign value to variable
   mov r10, [MEMORY + 36]
   add rax, r10
   mov [MEMORY + 36], DWORD eax
   push rax
   jmp .L71
   .L104: ; WHILE END
   push 1
   pop rax ; return value
   leave
   ret
   leave
   ret
 _syscall:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 40], rdi
   mov [MEMORY + 48], rsi
   mov [MEMORY + 56], rdx
   mov [MEMORY + 64], rcx
   mov rax, 0 ; store variable ret
   mov [MEMORY + 72], rax
   mov    rax, [MEMORY + 40]
   mov    rdi, [MEMORY + 48]
   mov    rsi, [MEMORY + 56]
   mov    rdx, [MEMORY + 64]
   syscall
   mov    [MEMORY + 72], rax
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 72]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 printstr:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 80], rdi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 80]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call strlen
   push rax
   pop rax ; store variable length
   mov [MEMORY + 88], eax
   push 1
   xor rdi, rdi
   pop rdi ; func call arg
   push 1
   xor rsi, rsi
   pop rsi ; func call arg
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 80]
   push rax
   xor rdx, rdx
   pop rdx ; func call arg
   xor rax, rax ; begin loading from var
   mov eax, DWORD [MEMORY + 88]
   push rax
   xor rcx, rcx
   pop rcx ; func call arg
   xor rax, rax
   call _syscall
   push rax
   pop rax ; store variable ret
   mov [MEMORY + 92], rax
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 92]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 println:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 100], rdi
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 100]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call printstr
   push rax
   pop rax ; store variable ret
   mov [MEMORY + 108], rax
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 100]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call strlen
   push rax
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 108]
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
   je .L215
   push 1
   xor rdi, rdi
   pop rdi ; func call arg
   push 1
   xor rsi, rsi
   pop rsi ; func call arg
   push str_0
   xor rdx, rdx
   pop rdx ; func call arg
   push 1
   xor rcx, rcx
   pop rcx ; func call arg
   xor rax, rax
   call _syscall
   push rax
   pop rax ; assign value to variable
   mov r10, [MEMORY + 108]
   add rax, r10
   mov [MEMORY + 108], QWORD rax
   push rax
   jmp .L215
 .L215: ; END IF STMT
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 108]
   push rax
   pop rax ; return value
   leave
   ret
   leave
   ret
 printint:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 116], rdi
   push str_1
   pop rax ; store variable buffer
   mov [MEMORY + 124], rax
   mov   rdi, [MEMORY + 116]
   mov   rsi, [MEMORY + 124]
   xor   rcx, rcx
   mov   rax, rdi
   test  rax, rax
   jns   .L1
   mov   BYTE [rsi], '-' ; Add sign
   neg   rax
   mov   rdi, rax
   add   rsi, 1
   .L1:    ; get length of number in characters
   mov   rbx, 10
   .L1A:
   add   rcx, 1
   cqo       ; convert quad to oct (rax to rdx:rax)
   div   rbx
   test  rax, rax
   jnz   .L1A
   mov   rax, rdi
   mov   BYTE [rsi+rcx], 0
   .L2:
   cqo
   div   rbx
   add   dl, '0'
   sub   rcx, 1
   mov   BYTE [rsi+rcx], dl
   test  rcx, rcx
   jnz   .L2
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 124]
   push rax
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax
   call printstr
   push rax
   push 0
   pop rax ; return value
   leave
   ret
   leave
   ret
 _clear_input:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 132], rdi
   push 0
   pop rax ; store array initializer
   mov [(MEMORY + 140) + 0], al
   .L290: ; WHILE START
   push 10
   xor rax, rax ; begin loading from var
   mov rax, MEMORY + 140
   push rax
   xor r10, r10
   xor r9, r9
   pop r9 ; array pointer
   push 0
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
   pop rax ; while condition start
   cmp rax, 0
   je .L312
   push 0
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 132]
   push rax
   xor rsi, rsi
   pop rsi ; func call arg
   xor rax, rax ; begin loading from var
   mov rax, MEMORY + 140
   push rax
   xor rdx, rdx
   pop rdx ; func call arg
   push 1
   xor rcx, rcx
   pop rcx ; func call arg
   xor rax, rax
   call _syscall
   push rax
   jmp .L290
   .L312: ; WHILE END
   leave
   ret
 read:
   push rbp
   mov rbp, rsp
   mov [MEMORY + 141], rdi
   mov [MEMORY + 149], rsi
   mov [MEMORY + 157], rdx
   push 0
   xor rdi, rdi
   pop rdi ; func call arg
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 141]
   push rax
   xor rsi, rsi
   pop rsi ; func call arg
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 149]
   push rax
   xor rdx, rdx
   pop rdx ; func call arg
   xor rax, rax ; begin loading from var
   mov rax, QWORD [MEMORY + 157]
   push rax
   xor rcx, rcx
   pop rcx ; func call arg
   xor rax, rax
   call _syscall
   push rax
   leave
   ret
 return_to_sender:
   push rbp
   mov rbp, rsp
   push 420
   pop rax ; negate top of stack
   neg rax
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
   str_1: db `123456789012345678901`, 0
   str_2: db ``, 0
