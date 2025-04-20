'''
stack -> LIFO
수열 만들기
ex) push push pop pop
[2, 1]

ex) push push push pop push pop push push pop pop
[3,4,6,5]

ex) NO
push pop push pop push push push pop 3을 못뺌 
[1,2,5,3,4]

% 수열의 어떤 뽀인트가 만들 수 없는 걸까
- 만약 5를 넣으면, 그 뒤는 무조건 5 밑으로 내림차순이여햐 함
    - ex) 5, 4, 2, 1 (O)
    - ex) 5, 2, 4 (X)

- 면 출력됨
+ 면 push
'''
import sys
input = sys.stdin.readline
# 넣으면서 테스트해볼거
stack = []
# 주어진 수열
_list = []
n = int(input().rstrip())
# 방문노드
visited = [False] * (n+1)

for _ in range(n):
    k = int(input().rstrip())
    _list.append(k)

# 수열 만들 수 있는 검사
max_num = max(_list)
for i in range(_list.index(max_num), len(_list)):
    stack.append(_list[i])

if stack != sorted(stack, reverse=True):
    print("NO")

stack = []
# + : 방문 안한것들 스택에 넣기
for j in range(n):
    for i in range(_list[j]):
        if not visited[i+1]:
            stack.append(i+1)
            print("+")
                 
        visited[i+1] = True
    # - : 스택에서 빼기
    if stack[-1] == _list[j]:
        stack.pop()
        print("-")
