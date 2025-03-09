package main

import (
	"fmt"
)

var board [3][3]string

// Function to initialize the game board
func initializeBoard() {
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			board[i][j] = " "
		}
	}
}

// Function to print the game board
func printBoard() {
	fmt.Println("\n")
	fmt.Println("-------------")
	for i := 0; i < 3; i++ {
		fmt.Print("| ")
		for j := 0; j < 3; j++ {
			fmt.Print(board[i][j] + " | ")
		}
		fmt.Println("\n-------------")
	}
}

// Function to check if a player has won
func checkWinner(player string) bool {
	// Check rows and columns
	for i := 0; i < 3; i++ {
		if board[i][0] == player && board[i][1] == player && board[i][2] == player {
			return true
		}
		if board[0][i] == player && board[1][i] == player && board[2][i] == player {
			return true
		}
	}

	// Check diagonals
	if board[0][0] == player && board[1][1] == player && board[2][2] == player {
		return true
	}
	if board[0][2] == player && board[1][1] == player && board[2][0] == player {
		return true
	}

	return false
}

// Function to check if the board is full (game tie)
func isBoardFull() bool {
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if board[i][j] == " " {
				return false
			}
		}
	}
	return true
}

// Function to handle player's turn
func playerTurn(player string) {
	var row, col int
	for {
		fmt.Printf("Player %s, enter row (0-2) and column (0-2): ", player)
		_, err := fmt.Scanf("%d %d", &row, &col)
		if err != nil || row < 0 || row > 2 || col < 0 || col > 2 || board[row][col] != " " {
			fmt.Println("Invalid input. Please try again.")
			continue
		}
		board[row][col] = player
		break
	}
}

func main() {
	var currentPlayer string
	initializeBoard()

	// Game loop
	for {
		printBoard()

		// Set the current player
		if currentPlayer == "X" {
			currentPlayer = "O"
		} else {
			currentPlayer = "X"
		}

		// Ask for the player's move
		playerTurn(currentPlayer)

		// Check if the current player has won
		if checkWinner(currentPlayer) {
			printBoard()
			fmt.Printf("Player %s wins!\n", currentPlayer)
			break
		}

		// Check if the board is full (tie game)
		if isBoardFull() {
			printBoard()
			fmt.Println("It's a tie!")
			break
		}
	}
}
