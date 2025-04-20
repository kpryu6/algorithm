package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func toggle(list []int, k int) {
	if list[k] == 0 {
		list[k] = 1
	} else if list[k] == 1 {
		list[k] = 0
	}
	return
}

func printSlice(list []int) {
	strList := make([]string, len(list))
	for i, val := range list {
		strList[i] = fmt.Sprintf("%d", val)
	}
	fmt.Println(strings.Join(strList, " "))
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	userInput, _ := reader.ReadString('\n')
	N, _ := strconv.Atoi(strings.TrimSpace(userInput))

	// switch
	switchList := make([]int, N)

	listInput, _ := reader.ReadString('\n')
	listInput = strings.TrimSpace(listInput)
	inputList := strings.Split(listInput, " ")

	for i := 0; i < N; i++ {
		switchList[i], _ = strconv.Atoi(inputList[i])
	}

	lenInput, _ := reader.ReadString('\n')
	peopleLen, _ := strconv.Atoi(strings.TrimSpace(lenInput))

	for i := 0; i < peopleLen; i++ {
		infoInput, _ := reader.ReadString('\n')
		personInfo := strings.Split(strings.TrimSpace(infoInput), " ")

		gender, _ := strconv.Atoi(personInfo[0])
		num, _ := strconv.Atoi(personInfo[1])

		// male
		if gender == 1 {
			for j := 0; j < N; j++ {
				if (j+1)%num == 0 {
					toggle(switchList, j)
				}
			}
		} else if gender == 2 {
			// female
			num = num - 1
			toggle(switchList, num)
			left := num - 1
			right := num + 1

			for left >= 0 && right < N && switchList[left] == switchList[right] {
				toggle(switchList, left)
				toggle(switchList, right)
				left = left - 1
				right = right + 1
			}
		}
	}

	// 출력
	if len(switchList) > 20 {
		for i := 0; i < len(switchList); i += 20 {
			end := i + 20
			if end > len(switchList) {
				end = len(switchList)
			}
			printSlice(switchList[i:end])
		}
	} else {
		printSlice(switchList[:N])
	}
}
