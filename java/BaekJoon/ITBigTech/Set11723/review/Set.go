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
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	mStr, _ := reader.ReadString('\n')
	mStr = strings.TrimSpace(mStr)
	m, _ := strconv.Atoi(mStr)

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
				for j := 0; j < 21; j++ {
					s[j] = struct{}{}
				}
			case "empty":
				s = make(map[int]struct{})
			}
		}
	}
}
