import sys
input = sys.stdin.readline


def dfs(del_node, parents):
    # 부모를 제거하는게 아니라 del_node를 트리에서 자르는 과정(부모를 -10으로 바꾸는거임)
    parents[del_node] = -10 # 의미없는 숫자를 부여해 제거함을 의미
    for i in range(N):
        # del_node를 부모로 가지고 있는 애들 모두 떨어뜨리기
        if del_node == parents[i]:
            dfs(i,parents)

N = int(input().rstrip())
parents = list(map(int, input().rstrip().split()))
dn = int(input().rstrip())

dfs(dn,parents)
count = 0

for i in range(N):
    # 제거된 노드도 아니고, i가 특정 노드의 부모가 아니면
    if parents[i] != -10 and i not in parents:
        count += 1

print(count)

    
