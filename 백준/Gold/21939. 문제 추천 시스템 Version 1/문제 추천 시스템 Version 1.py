import heapq
import sys
input = sys.stdin.readline

max_heap = []
min_heap = []
# 문제 리스트
problems = {}

N = int(input().rstrip())
for _ in range(N):
    P, L = map(int, input().rstrip().split())
    problems[P] = L
    heapq.heappush(max_heap, (-L, -P)) # 난이도, 번호 내림차순
    heapq.heappush(min_heap, (L,P)) # 난이도, 번호 오름차순

M = int(input().rstrip())
for _ in range(M):
    cmd = input().rstrip().split()

    if cmd[0] == "add":
        P, L = int(cmd[1]), int(cmd[2])
        problems[P] = L
        heapq.heappush(max_heap, (-L, -P))
        heapq.heappush(min_heap, (L,P))
    elif cmd[0] == "solved":
        P = int(cmd[1])
        if len(problems) > 0 and P in problems:
            # heap에는 아직 남아있음
            del problems[P]
    elif cmd[0] == "recommend":
        if cmd[1] == '1':
            while max_heap:
                L, P = heapq.heappop(max_heap)
                if -P in problems and problems[-P] == -L:
                    print(-P)
                    # 다시 넣어주기
                    heapq.heappush(max_heap, (L,P))
                    break
        elif cmd[1] == '-1':
            while min_heap:
                L, P = heapq.heappop(min_heap)
                if P in problems and problems[P] == L:
                    print(P)
                    heapq.heappush(min_heap, (L,P))
                    break

