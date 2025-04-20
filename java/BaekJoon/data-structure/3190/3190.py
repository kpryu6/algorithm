'''
끝: 벽, 자기자신 몸과 부딪힐 시

뱀 길이 = 1
초마다 이동

사과 존재: 꼬리는 그대로 놔두고 이동
사과 없음: 꼬리와 함께 몸 다같이 이동

자기자신 몸을 어떻게 구현하지
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())

board = [[0] * N for _ in range(N)]

for _ in range(K):
    r,c = map(int, input().rstrip().split())
    board[r-1][c-1] = 1

dir = []
L = int(input().rstrip())
for _ in range(L):
    sec, mv = input().rstrip().split()
    dir.append((int(sec),mv))

# 방향: 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 뱀 초기 상태
time = 0
snake = deque([(0,0)])
cur_dir = 0 # 처음엔 오른쪽
dir_idx = 0

while True:
    print(snake)
    time += 1
    # 뱀 머리
    head_x, head_y = snake[-1]
    nx = head_x + dx[cur_dir]
    ny = head_y + dy[cur_dir]

    # 벽이나 몸과 부딪힘
    if not (0 <= nx < N and 0 <= ny < N) or (nx,ny) in snake:
              break

    # 이동한 위치 처리
    # 사과 존재
    if board[nx][ny] == 1:
        board[nx][ny] = 0 # 사과 냠
        snake.append((nx,ny)) # 뱀 길이 증가
    # 사과 없으면
    else:
        snake.append((nx,ny)) # 머리를 늘리고
        snake.popleft() # 꼬리를 줄임
    
    # 방향 전환 시간 체크
    if dir_idx < len(dir) and time == dir[dir_idx][0]:
        if dir[dir_idx][1] == 'L': # Left
              cur_dir = (cur_dir - 1) % 4
        elif dir[dir_idx][1] == 'D': # right
              cur_dir = (cur_dir + 1) % 4
        dir_idx += 1

print(time)
