import sys

# 입력받는 버퍼생성해서 입력받음
input = sys.stdin.readline

N = int(input())
# 개행문자 제거
S = input().rstrip()

result = ''

for i in S:
    if i.islower():
        result += i.upper()
    elif i.isupper():
        result += i.lower()

print(result)
