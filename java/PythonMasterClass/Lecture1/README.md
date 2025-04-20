# Lecture1

## 1. UpperLower

- input
  - 입력문자열을 문자단위로 읽음
  - 개행 문자 삭제
  - 문자를 문자열로 변환
- 많은 입력 = Timeout

</br>

**sys.stdin.readline**
- 입력을 받는 버퍼 생성
- 버퍼에서 입력을 받아들임

**input().rstrip()**
- 개행 문자 제거

```python3
import sys
input = sys.stdin.readline
input().rstrip()
```

**str.islower(), str.isupper()**
- str이 모두 소문자인지 대문자인지 판별

**str.lower(), str.upper()**
- str을 소문자로, 대문자로 치환

**str.swapcase()**
- str의 대문자를 소문자로, 소문자를 대문자로 치환

</br>

---

## 2. WordFilter

**map(Function, iterable Data)**
```python3
N, M = map(int, input().split())
# 여기서 input().split() -> list로 리턴
# 1 2 3 -> ['1', '2', '3']
# int 적용해서 [1,2,3]
print(N, M)
```

**A.find(B)**
- A 문자열에서 B 문자열이 처음 등장하는 인덱스 추출

**A.replace(B, '')**
- A 문자열에서 B 문자열을 ''로 대체 (삭제)

</br>

---

## 3. FindBigger

**eval(A)**
- A라는 문자열이 수식이라면 수식의 결과를 반환 (우선순위 고려)

</br>
