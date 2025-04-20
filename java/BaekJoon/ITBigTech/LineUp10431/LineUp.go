package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func bubbleSort(list []int) int {
	steps := 0
	for i := len(list) - 1; i > 0; i-- {
		for j := 0; j < i; j++ {
			if list[j] > list[j+1] {
				list[j], list[j+1] = list[j+1], list[j]
				steps++
			}
		}
	}
	return steps
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	inputString, _ := reader.ReadString('\n')
	T, _ := strconv.Atoi(strings.TrimSpace(inputString))

	for i := 0; i < T; i++ {
		line, _ := reader.ReadString('\n')
		splits := strings.Split(strings.TrimSpace(line), " ")
		N := splits[0]
		x := make([]int, len(splits)-1)
		for j := 1; j < len(splits); j++ {
			x[j-1], _ = strconv.Atoi(splits[j])
		}
		fmt.Println(N, bubbleSort(x))
	}
}
