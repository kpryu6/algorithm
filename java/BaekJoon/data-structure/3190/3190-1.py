'''
벽, 몸과 부딪히면 끝
사과: 머리 전진 후 꼬리 그대로
사과x: 머리 전진 후 꼬리도 전진

언제끝나나?
'''
from collections import deque

# 보드 크기
N = int(input())

# 사과 개수
K = int(input())

board = [[0]*N for _ in range(N)]

# 사과의 위치
for _ in range(K):
    x,y = map(int,input().split())
    board[x-1][y-1] = 1

# 뱀 방향 변환 횟수
L = int(input())

dir = []
# 뱀 방향 변환 정보
for _ in range(L):
    X, C = input().split()
    dir.append((int(X),C))

time = 0
# 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]
snake = deque([(0,0)])
cur_d = 0

while True:
    # print(snake)
    time += 1
    head_x, head_y = snake[-1]
    nx = head_x + dx[cur_d]
    ny = head_y + dy[cur_d]

    # 벽 or 몸 -> 끝
    if not (0 <= nx < N and 0 <= ny < N) or (nx,ny) in snake:
        break

    # 사과O -> 머리 넣기(꼬리 그대로)
    if board[nx][ny] == 1:
        board[nx][ny] = 0
        snake.append((nx,ny))
    # 사과X -> 꼬리 빼기
    else:
        snake.append((nx,ny))
        snake.popleft()

    # 방향 전환
    for sec, mv in dir:
        if time == sec:
            if mv == 'D':
                cur_d = (cur_d + 1) % 4
            elif mv == 'L':
                cur_d = (cur_d - 1) % 4

print(time)



















