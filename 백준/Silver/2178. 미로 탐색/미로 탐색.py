'''
칸 이동 문제
dx dy 써야할듯?
'''
'''
4 6 # 행 열 # N M
101111
101010
101011
111011

15
'''
from collections import deque
import sys
input = sys.stdin.readline

graph = list()
N, M = map(int, input().split())
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

def bfs(x,y):

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 먼저!!!!
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[N-1][M-1]

print(bfs(0,0))
