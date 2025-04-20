package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Person struct {
	weight int
	height int
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	input = strings.TrimSpace(input)
	N, _ := strconv.Atoi(input)

	people := make([]Person, N)

	for i := 0; i < N; i++ {
		input, _ := reader.ReadString('\n')
		input = strings.TrimSpace(input)
		splits := strings.Split(input, " ")

		weight, _ := strconv.Atoi(splits[0])
		height, _ := strconv.Atoi(splits[1])

		people[i] = Person{weight, height}
	}

	for i := 0; i < N; i++ {
		rank := 1
		for j := 0; j < N; j++ {
			if people[i].height < people[j].height && people[i].weight < people[j].weight {
				rank += 1
			}
		}
		if i == N-1 {
			fmt.Println(rank)
		} else {
			fmt.Print(rank, " ")
		}
	}
}
