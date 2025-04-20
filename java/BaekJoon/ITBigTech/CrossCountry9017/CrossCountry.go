package main

import (
    "fmt"
    "strings"
    "strconv"
    "os"
    "bufio"
    "sort"
)

type Position struct {
    pos int
    team int
}

func main() {
    reader := bufio.NewReader(os.Stdin)
    T, _ := strconv.Atoi(readLine(reader))

    for i := 0; i < T; i++ {
        _ = readLine(reader) // 사용안해서 버림
        teams := strings.Split(readLine(reader), " ")

        teamMembers := make(map[int][]int)

        // 팀별 기록
        for idx, t := range teams {
            team, _ := strconv.Atoi(t)
            teamMembers[team] = append(teamMembers[team],idx+1)
        }

        validTeams := make(map[int][]int)
        for team, members := range teamMembers {
            if len(members) >= 6 {
                validTeams[team] = members
            }
        }

        // 유효한 팀 대상 새로운 순위 및 점수
        var allRanks []Position
        for team, members := range validTeams {
            for _, pos := range members {
                allRanks = append(allRanks, Position{pos, team})
            }
        }

        // pos 기준으로 정렬
        sort.Slice(allRanks, func(i, j int) bool {
            return allRanks[i].pos < allRanks[j].pos
        })

        scoreList := make(map[int][]int)
        for i, p := range allRanks {
            scoreList[p.team] = append(scoreList[p.team], i+1)
        }

        // 상위 4명 점수 계산 및 우승팀
        minScore := int(^uint(0) >> 1) // 최대 정수값
        winner := -1
        for team, scores := range scoreList {
            teamScore := sum(scores[:4])
            if teamScore < minScore {
                minScore = teamScore
                winner = team
            } else if teamScore == minScore {
                if scores[4] < scoreList[winner][4] {
                    winner = team
                }
            }
        }
        fmt.Println(winner)
    }
}

func readLine(reader *bufio.Reader) string {
    line, _ := reader.ReadString('\n')
    return strings.TrimSpace(line)
}

func sum(slice []int) int {
    total := 0
    for _, num := range slice {
        total += num
    }
    return total
}


