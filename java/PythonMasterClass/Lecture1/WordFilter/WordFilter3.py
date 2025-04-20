import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = input().rstrip()
E = input().rstrip()

while S in E:
    # replace 메소드를 통한 E에서 S 단어 계속 삭제
    E = E.replace(S, '')

if E:
    print(E)
else:
    print("EMPTY")
