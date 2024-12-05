'''
A는 A끼리
B는 B끼리
단어 위로 아치형 곡선

괄호 문제 ()
'''
import sys
input = sys.stdin.readline
ans = 0

N = int(input().rstrip())

for _ in range(N):
    # 괄호 창고
    stack = []
    words = list(input().rstrip())

    for i in words:
        if not len(stack):
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if not len(stack):
        ans += 1

print(ans)
