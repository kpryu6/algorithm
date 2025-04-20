'''
5 # 문제 개수 N
# N줄 
1000 1 # 문제번호 P, 난이도 L
1001 2
19998 78
2667 37
2042 55

8 # 명령문 개수 M
# M개의 명령문
add 1402 59
recommend 1
solved 1000
solved 19998
recommend 1
recommend -1
solved 1001
recommend -1

---
recommend 시 문제 번호 한줄씩 출력

# add P L
- 난이도 L인 문제번호 P 추가
(있던 P가 다른 L로 들어올 수 있음)

# solved P
- P 제거

# recommend x
- if x == 1
    가장 어려운거
    if 여러개
        P 큰거
- if x == -1
    가장 쉬운거
    if 여러 개
        P 작은거
'''
import sys
input = sys.stdin.readline

qlist = []

N = int(input().rstrip())
for _ in range(N):
    P, L = map(int, input().rstrip().split())
    qlist.append((P,L))
M = int(input().rstrip())
for _ in range(M):
    cmd = list(input().rstrip().split())

    if cmd[0] == "add":
        qlist.append((int(cmd[1]), int(cmd[2])))
    elif cmd[0] == "solved":
        if len(qlist) > 0:
            qlist = [item for item in qlist if item[0] != int(cmd[1])]
    elif cmd[0] == "recommend":
        qlist.sort(key=lambda x : (-x[-1], -x[0]))
        if cmd[1] == '1':
            print(qlist[0][0])
        else:
            print(qlist[-1][0])

