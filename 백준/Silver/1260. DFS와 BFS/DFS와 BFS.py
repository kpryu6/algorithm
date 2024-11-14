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


N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]
v_dfs = [False] * (N+1)
v_bfs = [False] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = True
    graph[e][s] = True

#for i in range(N+1):
    #print(graph[i])

def bfs(V):
    q = deque()
    q.append(V)
    v_bfs[V] = True

    while q:
        # deque에 append 시 오른쪽이 입구임
        # 1부터 3까지 append 시 (1,2,3) 됨
        # q.pop() = 3
        # q.popleft() = 1 # 그래서 bfs가 가능
        cur = q.popleft()
        print(cur, end=" ")
        for i in range(1,N+1):
            if not v_bfs[i] and graph[cur][i]: # if문에서 찾아도 너비탐색이기 때문에 계속 for문 돌아감(주위에 있는거 다 찾기)
                q.append(i)
                v_bfs[i] = True

def dfs(V):
    v_dfs[V] = True
    print(V, end=" ")
    for i in range(1, N+1):
        if not v_dfs[i] and graph[V][i]: # if문에서 찾아버리면 깊이 탐색해야 하기 때문에 dfs로 다시 가기 (계속 안으로 들어가기)
            v_dfs[i] = True
            dfs(i)
dfs(V)
print()
bfs(V)



