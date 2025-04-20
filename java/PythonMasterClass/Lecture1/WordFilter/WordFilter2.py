import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = input().rstrip()
E = input().rstrip()

while S in E:
    # S가 처음으로 등장하는 인덱스 추출
    idx = E.find(S)
    # 문자열에서 idx에 해당하는 인덱스 지우는 반복문
    for _ in range(len(S)):
        E = E[:idx] + E[idx + 1:]

if E:
    print(E)
else:
    print("EMPTY")
