import sys
input = sys.stdin.readline

N = int(input().rstrip())
stack = []
for _ in range(N):
    cmd = list(input().rstrip().split())
    op = cmd[0]

    if op == 'push':
        stack.append(int(cmd[1]))
    elif op == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif op == 'size':
        print(len(stack))
    elif op == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif op == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            top = stack.pop()
            print(top)
            stack.append(top)


