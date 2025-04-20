import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().rstrip())
tree = defaultdict(list)

for _ in range(N):
    node, lt, rt = input().rstrip().split()
    tree[node].append(lt)
    tree[node].append(rt)

# for i in tree:
    # print(i, tree[i])

# 전위순회 (루트 왼자 오자)
def preorder(root):
    if root != '.':
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위순회 (왼자 루트 오자)
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])

# 후위순회 (왼자 오자 루트)
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')

