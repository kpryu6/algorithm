'''
집이 모여있는데, 단지를 정해야댐

단지수 출력
각 단지의 집 수 출력 (오름차순)

일단 0,0부터 시작해야겠지

bfs로 계속 연결하다가 끊기면 거기까지가 한 단지
재귀?

끊긴다음은 어떻게해?
어떻게 다음 단지를 찾을까
그냥 for문 2개로 싹 돌아야할듯?
'''
'''
7 # 지도 크기
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3 # 총 단지 수
7 # 단지만큼의 단지 내 집 수 (리스트로 저장해야할듯)
8
9
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
graph = []
ans = list()

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# for i in range(N):
    # print(graph[i])
visited = [[False] * N for _ in range(N)]

def dfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    house = 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                house += dfs(nx,ny)

    return house

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            ans.append(dfs(i,j))



print(len(ans))
ans.sort()
for x in ans:
    print(x)