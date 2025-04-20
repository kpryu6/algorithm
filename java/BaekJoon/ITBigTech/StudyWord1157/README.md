# Go

## bufio.NewScanner vs bufio.NewReader

**bufio.NewScanner**

- 한줄을 읽어오기 위해 설계됨
- 기본적으로 최대 64KB의 입력 길이 처리 가능
- 64KB 초과시 sc.Scan() 실패 후 false 반환
- sc.Text()는 빈 문자열이 됨

**bufio.NewReader**

- 기본적으로 4KB의 버퍼 사용
- ReadString이 필요한 만큼 반복적으로 버퍼 사용하여 입력 읽음
- 입력 길이에 제한이 없음

**bufio.NewScanner 사용 시**

```go
// 커스텀 버퍼
// sc.Buffer()로 Scanner의 Buffer 크기를 설정
// 최대 읽기 길이 늘리기 가능
sc := bufio.NewScanner(os.Stdin)
buf := make([]byte, 0, 64*1024)
sc.Buffer(buf, 1024*1024)
```
