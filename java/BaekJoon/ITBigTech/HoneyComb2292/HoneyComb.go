package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
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
	k, err := strconv.Atoi(userInput)

	var n int = 1

	for {
		if k == 1 {
			break
		} else if 3*n*n+3*n+1 >= k {
			n += 1
			break
		}
		n += 1
	}
	fmt.Println(n)

}
