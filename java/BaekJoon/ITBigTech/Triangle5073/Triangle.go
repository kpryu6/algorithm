package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {

	var inputs [][]int
	sc := bufio.NewScanner(os.Stdin)

	for {
		// 다음 라인 읽기
		sc.Scan()
		// strings.Trimspace() : 문자열 양쪽 끝에서 공백 문자 제거
		// sc.Text() : 가장 최근의 라인을 문자열로 반환
		userInput := strings.TrimSpace(sc.Text())
		if userInput == "0 0 0" {
			break
		}

		// 문자열을 공백 문자로 분리하여 슬라이스(slice)로 반환
		params := strings.Fields(userInput)
		if len(params) != 3 {
			fmt.Println("파라미터는 3개여야 합니다.")
			continue
		}

		values := make([]int, 3)
		valid := true

		for i, param := range params {
			value, err := strconv.Atoi(param)
			if err != nil || value <= 0 || value > 1000 {
				fmt.Println("0초과 1000 이하여야함")
				valid = false
				break
			}
			values[i] = value
		}

		if valid {
			inputs = append(inputs, values)
		} else {
			fmt.Println("모든 파라미터는 정수이어야 함")
		}
	}

	for _, data := range inputs {
		a, b, c := data[0], data[1], data[2]

		// 삼각형 유효성 검사
		if a+b > c && a+c > b && b+c > a {
			// 모든 변이 같을 때
			if a == b && b == c {
				fmt.Println("Equilateral")
			} else if a == b || b == c || a == c {
				fmt.Println("Isosceles")
			} else {
				fmt.Println("Scalene")
			}
		} else {
			fmt.Println("Invalid")
		}
	}
}
