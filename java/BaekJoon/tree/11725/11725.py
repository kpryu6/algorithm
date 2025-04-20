import sys
from collections import defaultdict, deque

tree = defaultdict(list)

N = int(input().rstrip())
for _ in range(N-1):
    s, e = map(int, input().rstrip().split())
    tree[s].append(e)
    tree[e].append(s)

parent = [0] * (N+1)
parent[1] = 0
# print(tree)

# 부모노드인 조건이 뭔데??
# 1은 이미 루트
# 1과 연결된 노드들은 자식임
# 그 자식들은 또 그 자식들의 부모임
# while deque로 풀어보자

q = deque()
q.append(1)

while q:
    cur = q.pop()
    for v in tree[cur]:
        if parent[v] == 0:
            parent[v] = cur
            q.append(v)

for i in range(2,N+1):
    print(parent[i])
