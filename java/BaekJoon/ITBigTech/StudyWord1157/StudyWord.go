package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// 이거 NewScanner로 하니까 틀렸음
	// NewScanner는 되도록 한줄씩 입력받을 때 사용하기

	// string 하나 입력받기
	reader := bufio.NewReader(os.Stdin)
	userInput, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println("입력 에러", err)
		return
	}
	userInput = strings.TrimSpace(userInput)
	userInput = strings.ToUpper(userInput)

	freqMap := make(map[rune]int)

	// 문자 빈도 수 계산
	for _, char := range userInput {
		freqMap[char]++
	}

	// 최대 빈도 수 계산
	maxFreq := 0
	for _, freq := range freqMap {
		// fmt.Println(freq)
		if freq > maxFreq {
			maxFreq = freq
		}
	}

	maxFreqCount := 0
	maxFreqWord := rune(0)

	for char, freq := range freqMap {
		if freq == maxFreq {
			maxFreqWord = char
			maxFreqCount++
		}
	}

	if maxFreqCount > 1 {
		fmt.Println("?")
	} else {
		fmt.Printf("%c\n", maxFreqWord)
	}

}
