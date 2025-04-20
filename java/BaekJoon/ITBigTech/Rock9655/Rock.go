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
	n, _ := strconv.Atoi(strings.TrimSpace(userInput))

	if n%2 == 1 {
		fmt.Println("SK")
	} else {
		fmt.Println("CY")
	}
}
