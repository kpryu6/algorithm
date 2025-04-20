import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input().rstrip())
G = []
for _ in range(N):
    G.append(list(map(int, input().rstrip())))

# for i in range(N):
    # print(G[i])

ans = list()
visited = [[False] * N for _ in range(N)]

def dfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    size = 1

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and G[nx][ny] == 1:
            size += dfs(nx,ny)
    
    return size

for i in range(N):
    for j in range(N):
        if not visited[i][j] and G[i][j] == 1:
            ans.append(dfs(i,j))

print(len(ans))
ans.sort()
for x in ans:
    print(x)
