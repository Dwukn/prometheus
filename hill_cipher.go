
package main
import (
  "fmt"
  "strings"
"math"
)
func mod26(a int) int {
return (a % 26 + 26) % 26
}
func hillCipher(text string, key [][]int, mode string) string {
// Convert text to numbers (A=0, B=1, ..., Z=25)
var textNumbers []int
for _, char := range strings.ToUpper(text) {
if char >= 'A' && char <= 'Z' {
textNumbers = append(textNumbers, int(char-'A'))
}
}
// Pad text to fit the matrix size
if len(textNumbers)%len(key) != 0 {
for i := 0; i < len(key)-len(textNumbers)%len(key); i++ {
textNumbers = append(textNumbers, 0)
}
}
// Encrypt or decrypt
var result []int
for i := 0; i < len(textNumbers); i += len(key) {
vector := textNumbers[i : i+len(key)]
var newVector []int
for r := 0; r < len(key); r++ {
sum := 0
for c := 0; c < len(key[r]); c++ {
if mode == "encrypt" {
sum += key[r][c] * vector[c]
} else {
sum += mod26(int(math.Round(float64(key[r][c])))) *
vector[c]
}
}
newVector = append(newVector, mod26(sum))
}
result = append(result, newVector...)
}
// Convert back to characters
var resultText string
for _, num := range result {
resultText += string(num + 'A')
}
return resultText
}
func main() {
text := "ACT"
key := [][]int{
{6, 24, 1},
{13, 16, 10},
{20, 17, 15},
}
enc := hillCipher(text, key, "encrypt")
dec := hillCipher(enc, key, "decrypt")
fmt.Println("Hill Cipher Encrypt:", enc)
fmt.Println("Hill Cipher Decrypt:", dec)
}
