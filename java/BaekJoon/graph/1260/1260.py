'''
DFS 탐색 결과
BFS 탐색 결과

정점 번호 작은거부터
더이상 방문 못하면 종료
1 ~ N
'''
'''
4 5 1 # N, M, V
1 2 # M개의 줄
1 3
1 4
2 4
3 4

1 2 4 3 # DFS
1 2 3 4 # BFS
'''
from collections import deque
import sys

input = sys.stdin.readline

# 입력
N, M, S = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = True
    graph[e][s] = True

# 방문여부
visited_dfs = [False for _ in range(N+1)]
visited_bfs = [False for _ in range(N+1)]

def bfs(S):
    # 탐색
    q = deque()
    q.append(S)
    visited_bfs[S] = True

    while q:
        cur_node = q.popleft()
        print(cur_node, end=" ")
        for i in range(1, N+1):
            if not visited_bfs[i] and graph[cur_node][i]: # if문에서 찾아도 너비탐색이기 때문에 계속 for문 돌아감(주위에 있는거 다 찾기)
                visited_bfs[i] = True
                q.append(i)

def dfs(S):
    visited_dfs[S] = True
    print(S, end=" ")
    for i in range(1, N+1):
        if not visited_dfs[i] and graph[S][i]: # if문에서 찾아버리면 깊이 탐색해야 하기 때문에 dfs로 다시 가기 (계속 안으로 들어가기)
            dfs(i)

dfs(S)
print()
bfs(S)





