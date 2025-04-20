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
	input := strings.Split(userInput, " ")

	N, _ := strconv.Atoi(input[0])
	game := input[1]

	names := make(map[string]struct{})

	for i := 0; i < N; i++ {
		name, _ := reader.ReadString('\n')
		name = strings.TrimSpace(name)
		names[name] = struct{}{}
	}

	if game == "Y" {
		fmt.Println(len(names))
	} else if game == "F" {
		fmt.Println(len(names) / 2)
	} else if game == "O" {
		fmt.Println(len(names) / 3)
	}

}
