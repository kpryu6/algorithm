'''
'''
import sys
import heapq
input = sys.stdin.readline

qlist = {}
max_heap = []
min_heap = []

# 문제 리스트 문제 수
N = int(input().rstrip())
for _ in range(N):
    P, L = map(int, input().rstrip().split())
    qlist[P] = L
    heapq.heappush(max_heap, (-L, -P))
    heapq.heappush(min_heap, (L,P))

# 명령문 개수
M = int(input().rstrip())
for _ in range(M):
    cmd = input().rstrip().split()
    if cmd[0] == "add":
        P, L = int(cmd[1]), int(cmd[2])
        qlist[P] = L
        heapq.heappush(max_heap, (-L, -P))
        heapq.heappush(min_heap, (L,P))
    elif cmd[0] == "solved":
        P = int(cmd[1])
        if P in qlist:
            del qlist[P]
    elif cmd[0] == "recommend":
        if cmd[1] == '1':
            while max_heap:
                L, P = heapq.heappop(max_heap)
                if -P in qlist and qlist[-P] == -L:
                    print(-P)
                    heapq.heappush(max_heap, (L, P))
                    break
        else:
            while min_heap:
                L, P = heapq.heappop(min_heap)
                if P in qlist and qlist[P] == L:
                    print(P)
                    heapq.heappush(min_heap, (L, P))
                    break


