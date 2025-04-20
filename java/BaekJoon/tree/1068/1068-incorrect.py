'''
노드 지우면 모든 자손이 트리에서 제거됨
리프 노드의 개수 구하기

해당 노드를 지우면 자손 모두 제거
해당 노드 밑으로 싹 없어짐

leaf 노드 특징
1. 붙어있는 노드가 무조건 1개임

트리로 표현했을 때 붙어있는 노드가 1개인 노드는 리프노드임

#--- 삭제된 노드의 부모 노드가 새로운 리프 노드가 될 가능을 고려 안했음---#

노드 제거 시 붙어있는 노드가 1개인 노드  개수 세면 되려나?

노드제거는 어떻게?
노드 삭제시 자손까지 제거하는 로직 만들기 (현재는 visited만 했음)
'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = defaultdict(list)
N = int(input().rstrip())
parents = list(map(int, input().rstrip().split()))
# 제거할 노드
dn = int(input().rstrip())

for i in range(len(parents)):
    #--- 부모가 -1인 노드를 무조건 0번노드로 해버림 ---# -> 잘못된 부분
    if parents[i] == -1:
        parents[i] = 0
    T[i].append(parents[i])
    T[parents[i]].append(i)
# print(T)
visited = [False] * N
visited[dn] = True
q = deque()

# 전체 leaf 노드개수 찾기
result = 0
for node in T:
    if len(T[node]) == 1:
        result += 1

def bfs(start):
    global result
    q.append(start)

    while q:
        cur = q.popleft()

        for next in T[cur]:
            print("next node", next)
            if visited[next] == False:
                visited[next] = True
                if len(T[next]) == 1:
                    result -= 1
                # cur의 next가 cur의 부모가 아니면 append
                if next != parents[cur]:
                    q.append(next)

if len(T[dn]) == 1:
    result -= 1
else:
    bfs(dn)

print(result)
