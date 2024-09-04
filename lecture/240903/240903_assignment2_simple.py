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
import sys
input = sys.stdin.readline

N, M, cur = map(int, input().split())
cur -= 1
H = list(map(int, input().split()))
Q = int(input().rstrip())
move_list = input().split()

ans = 0
moves = {
	'L' : -1,
	'R' : 1,
	'S' : 0
}

i = 0
for m in move_list:
	if H[cur] + i >= M:
		ans += H[cur] + i
		H[cur] = -i
	
	cur = (cur + moves[m]) % N
	i += 1
	
print(ans)


