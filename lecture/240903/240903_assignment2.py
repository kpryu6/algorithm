'''
내용
원형모양의 나무들
높이가 M 이상인 나무들만 벌목, Q번 벌목
벌목 시, 목재량 += 나무높이 -> 그 나무(x)는 높이 0됨
L, R, S
높이가 1씩 자람

입력
4 3 1 # 나무수 # 높이제한 # 구름이 위치
2 0 1 5 # 나무 높이
5 # 벌목횟수(Q)
S R R L L # 움직일 방법

출력
소지한 목재량!
'''
'''
예시 2번 
4 0 2 3
위치 : 1 -> 나무 높이 0 -> 현재 목재량 : 0
5 1 3 4
위치 : 0 -> 나무 높이 5 -> 현재 목재량 : 5
1 2 4 5
위치 : -1 -> 나무 높이 5 -> 현재 목재량 : 10
2 3 5 1
위치 : -2 -> 나무 높이 5 -> 현재 목재량 : 15
'''
'''
import sys
input = sys.stdin.readline

N, M, cur = map(int, input().split())
heights = list(map(int, input().split()))
Q = int(input().rstrip())
move_list = input().split()

ans = 0
moves = {
	'L' : -1,
	'R' : 1,
	'S' : 0
}

# 나무 높이 1씩 증가하는 함수
def increase_all(arg_list):
	for i in range(len(arg_list)):
		arg_list[i] += 1

current = cur - 1

for move in move_list:
	if heights[current] >= M:
		ans += heights[current]
		heights[current] = 0
		
	current = current + moves[move]
	increase_all(heights)

print(ans)


# Timeout이 뜨는데, 아무래도 나무높이 1씩 증가하는게 부하가 큰가보다. 중첩 for문이 되어버려서?
'''

# Timeout 수정
# 나무의 높이를 하나씩 다 for문으로 돌려서 증가시키는게 아니라
# current_time을 두어서 해당 상황에 맞게 height 증가시키기

import sys
input = sys.stdin.readline

N, M, cur = map(int, input().split())
heights = list(map(int, input().split()))
Q = int(input().rstrip())
move_list = input().split()

ans = 0
moves = {
	'L' : -1,
	'R' : 1,
	'S' : 0
}

current_time = 0
current = cur - 1

for move in move_list:
	height = heights[current] + current_time
	if height >= M:
		ans += height
		# 이게 하이라이트네
		# 벌목 시점과 이후의 성장을 고려
		# ex) current_time이 5일 때, heights[current]가 -4였다면 실제 높이는 1임.
		# 벌목 후 1만큼 자랐다는 뜻
		heights[current] = 0 - current_time

	# index 번호 유지 해주기
	current = (current + moves[move]) % N
	current_time += 1

print(ans)


