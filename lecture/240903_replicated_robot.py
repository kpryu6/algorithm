'''
10 10 # 초기좌표
5 # 웅덩이 개수

# 웅덩이 좌표
11 10
10 9
10 11
9 9
9 11

4 # 이동횟수
R L U L
'''

import sys
input = sys.stdin.readline

x, y = map(int, input().split())
N = int(input().rstrip())

P = set() # Set으로 만드는 것 권장
# 제한된 검색 구간이 필요한 경우 무조건 Set
# 검색 시간이 없음 O(1)
# 리스트는 O(n)

for _ in range(N):
	a, b = map(int, input().split())
	P.add((a,b))
	# 웅덩이의 좌표를 관리하는 변수
	
M = int(input().rstrip())
# readline을 사용하게 되면 rstrip()으로 공백을 없애야 함

command_list = input().split()

# 좌표는 딕셔너리~~
moves = {
	'L' : (-1,0),
	'R' : (1, 0),
	'U' : (0, 1),
	'D' : (0, -1),
}

for move in command_list:
	a, b = moves[move]
	nX = x + a
	nY = y + b
	
	if (nX, nY) not in P:
		x = nX
		y = nY

print(x,y)
		
'''
DX/DY 기법
- 2차원 배열에서 좌표 이동 방법

dx = [0, 0, 1 ,-1]
dy = [1, -1, 0, 0]

nx = x + dx[0]
ny = y + dy[0]
'''

