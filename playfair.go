// playfair
package main
import (
"fmt"
"strings"
)
func createPlayfairMatrix(key string) [5][5]rune {
var matrix [5][5]rune
key = strings.ToUpper(key)
seen := map[rune]bool{}
alphabet := "ABCDEFGHIKLMNOPQRSTUVWXYZ"
// Remove duplicates and 'J' from key
var filteredKey string
for _, c := range key {
if c != 'J' && !seen[c] {
seen[c] = true
filteredKey += string(c)
}
}
// Fill the matrix with key then the rest of the alphabet
keyIndex := 0
for i := 0; i < 5; i++ {
for j := 0; j < 5; j++ {
if keyIndex < len(filteredKey) {
matrix[i][j] = rune(filteredKey[keyIndex])
keyIndex++
} else {
for _, c := range alphabet {
if !seen[c] {
matrix[i][j] = c
seen[c] = true
break
}
}
}
}
}
return matrix
}
func playfairCipher(text, key string, mode string) string {
var result strings.Builder
matrix := createPlayfairMatrix(key)
text = strings.ToUpper(text)
text = strings.ReplaceAll(text, "J", "I")
// Split text into digraphs
  var digraphs []string
for i := 0; i < len(text); i++ {
if i+1 < len(text) && text[i] != text[i+1] {
digraphs = append(digraphs, string(text[i:i+2]))
i++
} else {
digraphs = append(digraphs, string(text[i])+"X")
}
}
// Encrypt or decrypt based on mode
for _, digraph := range digraphs {
a, b := digraph[0], digraph[1]
var (row1, col1, row2, col2 int)
// Find positions of the letters
for i := 0; i < 5; i++ {
for j := 0; j < 5; j++ {
if matrix[i][j] == rune(a) {
row1, col1 = i, j
}
if matrix[i][j] == rune(b) {
row2, col2 = i, j
}
}
}
if row1 == row2 {
if mode == "encrypt" {
result.WriteRune(matrix[row1][(col1+1)%5])
result.WriteRune(matrix[row2][(col2+1)%5])
} else {
result.WriteRune(matrix[row1][(col1-1+5)%5])
result.WriteRune(matrix[row2][(col2-1+5)%5])
}
} else if col1 == col2 {
if mode == "encrypt" {
result.WriteRune(matrix[(row1+1)%5][col1])
result.WriteRune(matrix[(row2+1)%5][col2])
} else {
result.WriteRune(matrix[(row1-1+5)%5][col1])
result.WriteRune(matrix[(row2-1+5)%5][col2])
}
} else {
result.WriteRune(matrix[row1][col2])
result.WriteRune(matrix[row2][col1])
}
}
return result.String()
}
func main() {
text := "HELLO WORLD"
key := "KEYWORD"
enc := playfairCipher(text, key, "encrypt")
dec := playfairCipher(enc, key, "decrypt")
fmt.Println("Playfair Cipher Encrypt:", enc)
fmt.Println("Playfair Cipher Decrypt:", dec)
}
