import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
q = deque() # 얘도 list임
for _ in range(N):
    command = list(input().rstrip().split())
    op = command[0]

    if op == 'push':
        q.append(int(command[1]))
    elif op == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif op == 'size':
        print(len(q))
    elif op == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif op == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif op == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)

'''
print("---")
dq = deque()
dq.append(1)
dq.append(2)
dq.append(3)

print(dq[0])
print(dq[1])
print(dq[-1])
'''
