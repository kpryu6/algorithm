import sys, heapq
input = sys.stdin.readline

q = []

N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())
    if x != 0:
        heapq.heappush(q, (abs(x),x))
    else:
        if len(q) == 0:
            print(0)
        else:
            d = heapq.heappop(q)
            print(d[1])
