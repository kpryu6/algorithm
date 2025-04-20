package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	reader := bufio.NewReader(os.Stdin)
	userInput, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println("입력 에러", err)
		return
	}

	userInput = strings.TrimSpace(userInput)
	userInput = strings.ToUpper(userInput)

	if len(userInput) > 1000000 {
		fmt.Println("단어의 길이는 1,000,000을 넘지 말아야 한다.")
		return
	}

	freqMap := make(map[rune]int)

	// freqMap에 넣기
	for _, word := range userInput {
		freqMap[word]++
	}

	// maxFreq 구하기
	var maxFreq int = 0
	for _, freq := range freqMap {
		if freq > maxFreq {
			maxFreq = freq
		}
	}

	var maxFreqCount int = 0
	maxFreqWord := rune('?')

	for word, freq := range freqMap {
		if maxFreq == freq {
			maxFreqCount++
			maxFreqWord = word
		}
	}

	if maxFreqCount > 1 {
		fmt.Println("?")
	} else {
		fmt.Printf("%c\n", maxFreqWord)
	}

}
