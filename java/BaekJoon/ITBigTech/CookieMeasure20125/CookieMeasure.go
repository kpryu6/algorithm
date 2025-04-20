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
	userInput = strings.TrimSpace(userInput)
	N, _ := strconv.Atoi(userInput)

	// head := make([]int, 2)
	// 이렇게 하면 [0 0]이 기본으로 돼서 추가하면 [0 0 3 3] 이래 됨

	// rows에 저장
	var rows []string
	var head []int

	var leftHand, rightHand, waist, leftLeg, rightLeg int

	for i := 0; i < N; i++ {
		userInput, _ := reader.ReadString('\n')
		userInput = strings.TrimSpace(userInput)
		rows = append(rows, userInput)
	}

	// head 따기
	for i := 0; i < len(rows); i++ {
		if strings.Contains(rows[i], "*") {
			head = append(head, i+2)
			head = append(head, strings.Index(rows[i], "*")+1)
			break
		}
	}

	// 나머지 몸
	for i := head[0] - 1; i < N; i++ {
		// 팔
		if i == head[0]-1 {
			// 왼팔
			for j := 0; j < head[1]-1; j++ {
				if rows[i][j] == '*' {
					leftHand++
				}
			}
			// 오른팔
			for j := head[1]; j < len(rows[0]); j++ {
				if rows[i][j] == '*' {
					rightHand++
				}
			}
		}
		// 허리
		if i >= head[0] && rows[i][head[1]-1] == '*' {
			waist++
		}
		// 다리
		if i >= head[0] {
			if rows[i][head[1]-2] == '*' && rows[i][head[1]] == '*' {
				leftLeg++
				rightLeg++
			} else if rows[i][head[1]-2] == '*' {
				leftLeg++
			} else if rows[i][head[1]] == '*' {
				rightLeg++
			}
		}

	}
	fmt.Println(head[0], head[1])
	fmt.Println(leftHand, rightHand, waist, leftLeg, rightLeg)

}
