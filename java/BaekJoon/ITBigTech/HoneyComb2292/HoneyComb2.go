package main

import (
	"fmt"
)

func main() {

	var n int = 1
	var k int

	_, err := fmt.Scan(&k)
	if err != nil {
		fmt.Println("입력 에러", err)
		return
	}

	for {
		if k == 1 {
			break
		} else if 3*n*n+3*n+1 >= k {
			n += 1
			break
		}
		n += 1
	}
	fmt.Println(n)

}
