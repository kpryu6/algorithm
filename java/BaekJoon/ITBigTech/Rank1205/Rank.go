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
	newScore, _ := strconv.Atoi(input[1])
	P, _ := strconv.Atoi(input[2])
    
    rank := 1
    
    var rankList []int
	listInput, _ := reader.ReadString('\n')
	listInput = strings.TrimSpace(listInput)
	rankInput := strings.Split(listInput, " ")
    
    if N > 0 {
        for i := 0; i < N; i++ {
            rank, _ := strconv.Atoi(rankInput[i])
            rankList = append(rankList, rank) 
        }
    }

    for i := 0; i < N; i++ {
        if newScore > rankList[i] {
            break
        } else if newScore == rankList[i] {
            break
        } else {
            rank++
        }
    }

    if N == P && N > 0 && newScore <= rankList[N-1] {
        fmt.Println(-1)
    } else {
        fmt.Println(rank)
    }
}
