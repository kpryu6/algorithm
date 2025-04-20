import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
answer = []
v = 0
for i in range(N):
	v += nums[i]

i = 0
while True:
    if v / 8 ** i > 1:
        i += 1
    else:
        for j in range(i-1, -1, -1):
            answer.append(str(v // 8 ** j))
            v = v % 8 ** j
        print("".join(answer))
        break
