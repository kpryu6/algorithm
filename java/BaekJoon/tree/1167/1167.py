'''
트리 지름 구하는 거

5 # 정점 개수
# 5개의 줄
1 3 2 -1 
2 4 4 -1
3 1 2 4 3 -1 # 3 정점이 1 정점과 거리가 2, 4 정점과 거리가 3
4 2 4 3 3 5 6 -1
5 4 6 -1
'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

T = defaultdict(list)
V = int(input().rstrip())
for _ in range(V):
    line = list(map(int, input().rstrip().split()))
    v = line[0]
    idx = 1
    while line[idx] != -1:
        next, d = line[idx], line[idx+1]
        T[v].append((next,d))
        idx += 2


q = deque()
q.append(1)

visited = [-1] * (V+1)
visited[1] = 0

def dfs(start, d):
    
    for next, next_d in T[start]:
        if visited[next] == -1:
            visited[next] = next_d + d
            dfs(next, visited[next])

dfs(1,0)

long_from_1 = visited.index(max(visited))

visited = [-1] * (V+1)
visited[long_from_1] = 0

dfs(long_from_1, 0)

print(max(visited))
