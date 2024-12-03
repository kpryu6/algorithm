'''
노드 삭제
1. 해당 노드 부터 자식까지 모두 삭제
2. 부모가 해당 노드 연결 삭제

'''
import sys
from collections import defaultdict
input = sys.stdin.readline

tree = defaultdict(list)
root = -1

N = int(input().rstrip())
parents = list(map(int, input().rstrip().split()))
dn = int(input().rstrip())

# tree에 저장
for node, parent in enumerate(parents):
    if parent == -1:
        root = node
    else:
        tree[parent].append(node)

# 노드 삭제 로직
def delete_node(node):
    # 부모가 해당 노드 연걸 삭제
    for parent, children in tree.items():
        if node in children:
            children.remove(node)
    # 재귀적으로 자식까지 삭제
    for child in tree[node]:
        delete_node(child)

    tree.pop(node)

# leaf 노드 count 로직
def count_leaf(node):
    # node가 leaf면
    if len(tree[node]) == 0:
        return 1
    count = 0
    # node의 자식이 leaf일 수 있음(재귀)
    for child in tree[node]:
        count += count_leaf(child)

    return count

if dn == root:
    print(0)
else:
    delete_node(dn)
    print(count_leaf(root))
