import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = defaultdict(list)
N = int(input())
q = deque()
for _ in range(N-1):
    s, e, d = map(int, input().split())
    T[s].append((e,d))
    T[e].append((s,d))

def bfs(start):

    visited = [-1] * (N+1)
    visited[start] = 0
    q.append(start)

    while q:
        cur = q.popleft()
        for next, next_d in T[cur]:
            if visited[next] == -1:
                visited[next] = visited[cur]+ next_d
                q.append(next)
    
    long_from_root = visited.index(max(visited))

    return [long_from_root, max(visited)]

print(bfs(bfs(1)[0])[1])



