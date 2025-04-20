from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 이게 Kick이네
    if graph[x][y] == 1:
        graph[x][y] = 0

        q = deque()
        q.append((x,y))
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx,ny))
        return True

    return False       



T = int(input().rstrip())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        i, j = map(int, input().split())
        graph[j][i] = 1

    cnt = 0

    for i in range(N):
        for j in range(M):
            if bfs(i,j):
                cnt += 1

    print(cnt)
