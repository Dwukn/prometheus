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
