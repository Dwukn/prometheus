package main

import (
	"fmt"
	"strings"
)

// Caesar cipher encryption function
func caesarCipher(text string, shift int) string {
	var encryptedText string
	// Convert the text to uppercase using strings package
	text = strings.ToUpper(text)
	for _, char := range text {
		if char >= 'A' && char <= 'Z' {
			// Encrypt uppercase letters
			encryptedText += string(((int(char)-65+shift)%26 + 26) % 26 + 65)
		} else if char >= 'a' && char <= 'z' {
			// Encrypt lowercase letters
			encryptedText += string(((int(char)-97+shift)%26 + 26) % 26 + 97)
		} else {
			// Non-alphabetic characters remain unchanged
			encryptedText += string(char)
		}
	}
	return encryptedText
}

func main() {
	text := "Hello, World!"
	shift := 3
	encryptedText := caesarCipher(text, shift)
	fmt.Println("Original Text:", text)
	fmt.Println("Encrypted Text:", encryptedText)
}

