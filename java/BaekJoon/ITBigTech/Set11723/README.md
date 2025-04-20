# Python

## input() vs sys.stdin.readline()

**input()**

- 표준 입력에서 한 줄을 읽어 문자열로 반환
- sys.stdin.readline() 내부적으로 사용 + 줄 끝 개행 문자 제거 + 프롬프트 처리
- 입력 여러번 호출 시 성능 떨어짐

**sys.stdin.readline()**

- 개행 문자 포함하므로 제거하려면 .strip() 필요
- 많은 양의 입력 처리 시 성능에 이점
