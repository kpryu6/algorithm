'''
바이러스 전염
연결되어 있으면 다 바이러스

7 # V
6 # E
1 2
2 3
1 5
5 2
5 6
4 7

4
'''
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

graph = defaultdict(list)

V = int(input())
E = int(input())
visited = [False] * (V+1)
for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# print(V,E, graph)

q = deque()
q.append(1)
visited[1] = True
ans = 0

while q:
    cur = q.popleft()
    # print(cur, end=" ")

    for next in graph[cur]:
        if not visited[next]:
            q.append(next)
            visited[next] = True
            ans += 1

print(ans)