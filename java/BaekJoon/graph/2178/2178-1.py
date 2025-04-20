'''
N,M 크기 배열
1 = 이동
0 = 벽
(1,1)에서 출발 -> (N,M)까지
서로 인접한 칸으로만 이동

배열에 칸 저장 - bfs
'''
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# for i in range(N):
    # print(graph[i])

# 좌표 찍는거니깐
def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x,y))

    # 1을 따라가면서 사방에 값 채우기
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] += graph[x][y]

bfs(0,0)
print(graph[N-1][M-1])
# for i in range(N):
    # print(graph[i])
'''
[3, 0, 9, 10, 11, 12]
[2, 0, 8, 0, 12, 0]
[3, 0, 7, 0, 13, 14]
[4, 5, 6, 0, 14, 15]
'''
