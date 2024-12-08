import sys
input = sys.stdin.readline

# cur 변수 하나 잡아서 놓기(인덱스) - 어디까지 왔는지 돌 세우기
n = int(input().rstrip())
_list = list(int(input().rstrip()) for _ in range(n))
# print(_list)

stack = []
op = []
cur = 1

for num in _list:
    while cur <= num:
        stack.append(cur)
        op.append("+")
        cur += 1
    if stack[-1] == num:
        stack.pop()
        op.append("-")
    else:
        print("NO")
        sys.exit()

for o in op:
    print(o)
        


