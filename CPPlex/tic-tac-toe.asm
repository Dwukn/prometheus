section .data
    prompt db "Player 1 (X), enter your move (1-9): $"
    prompt2 db "Player 2 (O), enter your move (1-9): $"
    board db '1', '2', '3', '4', '5', '6', '7', '8', '9', 0  ; Game board

    win_msg db "We have a winner!$"
    draw_msg db "It's a draw!$"
    newline db 0xA, 0xD, '$'  ; Newline

section .bss
    move resb 1

section .text
    global _start

_start:
    ; Main game loop
    ; This game will alternate between Player 1 and Player 2
    call display_board
game_loop:
    ; Player 1's turn
    call player_move_1
    call display_board
    call check_win
    ; If Player 1 wins, jump to win message
    test al, al
    jz player_2_turn

    ; Player 2's turn
player_2_turn:
    call player_move_2
    call display_board
    call check_win
    ; If Player 2 wins, jump to win message
    test al, al
    jz game_loop

    ; Repeat game loop

; Display the board
display_board:
    ; Display the board in a 3x3 grid
    ; print each character in board array
    mov si, board
    mov di, 0
    
    ; Print the first row
    mov ah, 0x0E    ; teletype output
    mov al, [si]    
    int 0x10         ; display character
    inc si
    mov al, ' '
    int 0x10
    inc si
    mov al, [si]    
    int 0x10
    inc si
    mov al, ' '
    int 0x10
    inc si
    ; Move to next line
    mov ah, 0x0E    ; teletype output
    mov al, 0x0A    ; newline
    int 0x10
    mov al, 0x0D    ; carriage return
    int 0x10

    ; Print second row
    ; Repeat above code for second and third rows
    ret

player_move_1:
    ; Get player 1's move
    mov ah, 0x09
    lea dx, [prompt]
    int 0x21 ; DOS interrupt (display prompt)
    
    ; Get input (move number)
    mov ah, 0x01   ; Read a character from standard input
    int 0x21       ; Input
    sub al, '0'     ; Convert ASCII to integer
    ; Store move in board
    ; We will assume player input is valid and not out of bounds
    ; (real game should add validation)
    movzx bx, al    ; Player's choice (1-9)
    movzx si, bx
    mov al, 'X'     ; Player 1 is X
    mov [board + si], al
    ret

player_move_2:
    ; Get player 2's move
    mov ah, 0x09
    lea dx, [prompt2]
    int 0x21 ; DOS interrupt (display prompt)
    
    ; Get input (move number)
    mov ah, 0x01   ; Read a character from standard input
    int 0x21       ; Input
    sub al, '0'     ; Convert ASCII to integer
    ; Store move in board
    movzx bx, al    ; Player's choice (1-9)
    movzx si, bx
    mov al, 'O'     ; Player 2 is O
    mov [board + si], al
    ret

check_win:
    ; Check for winning conditions
    ; 3 possible rows, columns and diagonals
    ; (e.g., [0,1,2], [3,4,5], etc.)
    ; Simple win checking logic for 3x3 grid (rows/columns/diagonals)
    ; If there’s a match, return 1
    ; If no winner, return 0
    ; Check rows
    ; Check if positions 0,1,2 are the same (and so on)
    ; If no winner, return to game loop
    ret
