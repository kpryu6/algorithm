'''
'''
import sys
import heapq
input = sys.stdin.readline

li = []

N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())
    if x > 0:
        # -x도 같이 push
        heapq.heappush(li, (-x,x))
    elif x == 0:
        if len(li) == 0:
            print(0)
        else: 
            print(heapq.heappop(li)[1])

