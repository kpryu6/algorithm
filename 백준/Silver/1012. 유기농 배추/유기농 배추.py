'''
인접 노드간에는 지렁이 1 필요
이거도 결국 그 그래픽에서 사이즈 구하는 문제
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

T = int(input().rstrip())

def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    size = 1

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
            size += bfs(nx,ny)

    return size

ans = list()

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        graph[j][i] = 1

    warms = list()

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                warms.append(bfs(i,j))

    ans.append(len(warms))

for x in ans:
    print(x)








#for i in range(N):
    #print(graph[i])

