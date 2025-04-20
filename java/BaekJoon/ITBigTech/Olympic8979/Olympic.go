package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Country struct {
	name   int
	gold   int
	silver int
	bronze int
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	userInput, _ := reader.ReadString('\n')
	userInput = strings.TrimSpace(userInput)
	input := strings.Split(userInput, " ")

	N, _ := strconv.Atoi(input[0])
	K, _ := strconv.Atoi(input[1])

	countries := make([]Country, N)

	for i := 0; i < N; i++ {
		userInput, _ := reader.ReadString('\n')
		userInput = strings.TrimSpace(userInput)
		input := strings.Split(userInput, " ")

		name, _ := strconv.Atoi(input[0])
		gold, _ := strconv.Atoi(input[1])
		silver, _ := strconv.Atoi(input[2])
		bronze, _ := strconv.Atoi(input[3])

		countries[i] = Country{name, gold, silver, bronze}
	}

	// 정렬
	sort.Slice(countries, func(i, j int) bool {
		if countries[i].gold != countries[j].gold {
			return countries[i].gold > countries[j].gold
		}
		if countries[i].silver != countries[j].silver {
			return countries[i].silver > countries[j].silver
		}
		return countries[i].bronze > countries[j].bronze
	})

	// target 찾기
	var target Country
	for _, country := range countries {
		if country.name == K {
			target = country
			break
		}
	}

	// target 순위 찾기
	rank := 1
	for i, country := range countries {
		if target.gold == country.gold && target.silver == country.silver && target.bronze == country.bronze {
			rank = i + 1
			break
		}
	}
	fmt.Println(rank)
}
