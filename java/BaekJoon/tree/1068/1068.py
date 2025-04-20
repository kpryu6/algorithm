'''
1. 삭제된 노드의 부모 노드가 새로운 리프 노드가 될 가능성 고려하기
2. 삭제 시 자손까지 삭제하는 로직 구현 필요
3. 부모가 -1인 노드를 0으로 고정 X

재귀+ 트리 문제
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().rstrip())
parents = list(map(int, input().rstrip().split()))
dn = int(input().rstrip())
root = -1
tree = defaultdict(list)

# 부모 : 자식들 로 표현
for child, parent in enumerate(parents):
    if parent == -1:
        root = child
    else:
        tree[parent].append(child)

# print(tree)

# 부모노드에서 해당 노드 제거 + 자식부터 자신까지 삭제
def delete_node(node):
    # 부모노드에서 이 node 제거
    for parent, children in tree.items():
        if node in children:
            children.remove(node)
    # child 삭제
    for child in tree[node]:
        delete_node(child)
    # node 삭제
    tree.pop(node)

def count_leaf(node):
    if len(tree[node]) == 0:
        return 1

    count = 0
    for child in tree[node]:
        count += count_leaf(child)
    return count
    

if dn == root:
    print(0)
else:
    delete_node(dn)
    print(count_leaf(root))
