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
		sc.Scan()
		userInput := strings.TrimSpace(sc.Text())
		if userInput == "0 0 0" {
			break
		}

		splits := strings.Fields(userInput)
		if len(splits) != 3 {
			fmt.Println("파라미터는 3개여야 합니다")
		}

		values := make([]int, 3)
		valid := true

		for i, split := range splits {
			value, err := strconv.Atoi(split)
			if err != nil || value <= 0 || value > 1000 {
				fmt.Println("각 파라미터는 1000을 넘지 않는 양의 정수여야 합니다.")
				valid = false
				break
			}
			values[i] = value
		}

		if valid {
			inputs = append(inputs, values)
		} else {
			break
		}
	}

	for _, data := range inputs {
		a, b, c := data[0], data[1], data[2]

		// 삼각형 유효성 검사
		if a+b > c && a+c > b && b+c > a {
			if a == b && b == c {
				// 세 변이 모두 같을 때
				fmt.Println("Equilateral")
			} else if a == b || b == c || a == c {
				// 두 변이 같을 때
				fmt.Println("Isosceles")
			} else {
				// 변이 모두 다를 때
				fmt.Println("Scalene")
			}
		} else {
			// 삼각형이 아닐 때
			fmt.Println("Invalid")
		}
	}
}
