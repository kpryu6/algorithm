import sys
input = sys.stdin.readline

# 삭제할 노드들은 -2로 만들기
def dfs(node, parents):
    parents[node] = -2
    for i in range(len(parents)):
        if node == parents[i]:
            dfs(i, parents)

N = int(input().rstrip())
parents = list(map(int, input().rstrip().split()))
dn = int(input().rstrip())

dfs(dn, parents)
count = 0

for i in range(len(parents)):
    # -2가 아니면서, 다른 노드의 부모노드가 아닌 원소를 찾을 때마다
    if parents[i] != -2 and i not in parents:
        count += 1
print(count)
