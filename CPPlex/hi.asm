section .data
    hello_message db 'Hello, World!', 0xA  ; The message to print, with a newline at the end

section .text
    global _start  ; The entry point for the program

_start:
    ; Write the message to stdout (file descriptor 1)
    mov eax, 1        ; syscall number for sys_write (1)
    mov ebx, 1        ; file descriptor 1 (stdout)
    mov ecx, hello_message  ; address of the message
    mov edx, 14       ; length of the message (13 characters + 1 for newline)
    syscall           ; make the system call

    ; Exit the program
    mov eax, 60       ; syscall number for sys_exit (60)
    xor ebx, ebx      ; return code 0 (success)
    syscall           ; make the system c
all
