package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// println("ZOAC4")
	reader := bufio.NewReader(os.Stdin)
	userInput, _ := reader.ReadString('\n') // 에러 생략

	// 문자열을 공백 문자 기준으로 분할하여 문자열 배열(slice)로 반환
	params := strings.Fields(userInput)

	// fmt.Println(userInput)
	// fmt.Println(params)

	if len(params) != 4 {
		fmt.Println("파라미터를 4개 입력하세요")
		return
	}

	// 4개짜리 배열 생성
	pv := make([]int, 4)

	// pv에 params 넣기
	for i, param := range params {
		// 문자열 정수로 반환
		value, err := strconv.Atoi(param)
		if err != nil || value <= 0 || value > 50000 {
			fmt.Println("각 파라미터는 0 초과 50000 미만이여야 함")
			return
		}
		pv[i] = value
	}

	H, W, N, M := pv[0], pv[1], pv[2], pv[3]

	checkRows := ((H - 1) / (N + 1)) + 1
	checkCols := ((W - 1) / (M + 1)) + 1

	answer := checkCols * checkRows
	fmt.Println(answer)
}
