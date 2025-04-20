package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// 표준 입력 버퍼링
	// ReadString('\n') 메서드로 한 줄씩 입력 읽음
	reader := bufio.NewReader(os.Stdin)

	// 표준 출력 버퍼링
	// Fprintln(writer, ...)로 출력 내용 버퍼에 기록
	writer := bufio.NewWriter(os.Stdout)

	// main 함수 종료될 때 Writer 버퍼 비움 (버퍼에 있는 데이터 모두 출력)
	defer writer.Flush()

	// 한 줄 입력받고 trimspace 후 int로 저장
	mStr, _ := reader.ReadString('\n')
	m, _ := strconv.Atoi(strings.TrimSpace(mStr))

	// 메모리를 사용하지 않는 빈 구조체
	// 키 만 사용
	s := make(map[int]struct{})

	for i := 0; i < m; i++ {
		cmd, _ := reader.ReadString('\n')
		cmd = strings.TrimSpace(cmd)
		cmdData := strings.Split(cmd, " ")

		op := cmdData[0]

		if len(cmdData) > 1 {
			num, _ := strconv.Atoi(cmdData[1])

			switch op {
			case "add":
				s[num] = struct{}{}
			case "remove":
				delete(s, num)
			case "check":
				if _, found := s[num]; found {
					fmt.Fprintln(writer, 1)
				} else {
					fmt.Fprintln(writer, 0)
				}
			case "toggle":
				if _, found := s[num]; found {
					delete(s, num)
				} else {
					s[num] = struct{}{}
				}
			}
		} else {
			switch op {
			case "all":
				for j := 1; j <= 20; j++ {
					s[j] = struct{}{}
				}
			case "empty":
				s = make(map[int]struct{})
			}
		}
	}
}
