package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

func isDouble(input string) bool {
	for i := 0; i < len(input)-1; i++ {
		if input[i] == input[i+1] && input[i] != 'e' && input[i] != 'o' {
			return false
		}
	}
	return true
}

func main() {

	// 모음 포함 유무
	isVowel := regexp.MustCompile(`[aeiou]`)
	// 자음이나 모음 3번 연속
	isTriple := regexp.MustCompile(`[aeiou]{3}|[^aeiou]{3}`)
	// ee와 oo를 제외한 같은 글자 2번 연속
	// isDouble()

	reader := bufio.NewReader(os.Stdin)

	for {
		input, _ := reader.ReadString('\n')
		input = strings.TrimSpace(input)
		if input == "end" {
			break
		}

		case1 := isVowel.MatchString(input)
		case2 := !isTriple.MatchString(input)
		case3 := isDouble(input)

		if case1 && case2 && case3 {
			fmt.Printf("<%s> is acceptable.\n", input)
		} else {
			fmt.Printf("<%s> is not acceptable.\n", input)
		}
	}
}
