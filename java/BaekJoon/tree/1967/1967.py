'''
트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이
root에서 leaf까지의 길이?
경로 하나하나 다 check?

root -> leaf 길이 다 구해서
가장 긴거 2개
공통경로 빼면 되지 않나?
공통 경로는 어떻게 구할건데

이게 아님

풀이
1. 시작 정점에서 임의의 정점까지 거리 구해서 가장 먼 거리 구함
2. 1에서 찾은 가장 먼 거리를 시작 정점으로 하여 다시 한번 가장 긴 거리 찾기
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 일단 경로 저장
T = defaultdict(list)
N = int(input().rstrip())
for _ in range(N-1):
    s, e, cost = map(int, input().rstrip().split())
    T[s].append((e, cost))
    T[e].append((s, cost))

# print(T)

visited = [-1] * (N+1)
visited[1] = 0

# 1번 구하기(DFS)
def dfs(start, d):
    for next, next_d in T[start]:
        if visited[next] == -1:
            visited[next] = d + next_d
            dfs(next, visited[next])

dfs(1,0)

# 2번 구하기
long_from_root = visited.index(max(visited))

visited = [-1] * (N+1)
visited[long_from_root] = 0
dfs(long_from_root, 0)

print(max(visited))






