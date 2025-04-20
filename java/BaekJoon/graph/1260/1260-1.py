'''
정점 번호 작은 거부터 먼저 방문
방문 할거 없으면 종료
1부터N
정점 1000
간선 10000

간선 양방향
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
            if not v_bfs[i] and graph[cur][i]:
                q.append(i)
                v_bfs[i] = True

def dfs(V):
    v_dfs[V] = True
    print(V, end=" ")
    for i in range(1, N+1):
        if not v_dfs[i] and graph[V][i]:
            v_dfs[i] = True
            dfs(i)
dfs(V)
print()
bfs(V)
