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
	userInput, _ := reader.ReadString('\n')
	splits := strings.Fields(userInput)

	if len(splits) != 4 {
		fmt.Println("파라미터 4개를 입력하세요")
		return
	}

	values := make([]int, 4)

	for i, split := range splits {
		value, err := strconv.Atoi(split)
		if err != nil || value <= 0 || value > 50000 {
			fmt.Println("파라미터는 0 초과 50000 이하여야함")
		}
		values[i] = value
	}

	H, W, N, M := values[0], values[1], values[2], values[3]
	check_rows := ((H - 1) / (N + 1)) + 1
	check_cols := ((W - 1) / (M + 1)) + 1
	answer := check_cols * check_rows
	fmt.Println(answer)

}
