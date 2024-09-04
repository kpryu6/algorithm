'''
5 # 각자 나열한 카드 개수 N
8 6 4 2 0 # Alice가 나열한 카드의 공격력
1 4 7 10 13 # Bob이 나열한 카드의 공격력

1 9 # 출력

이기면 +2

차이가 7이면,
공격력 낮은 사람이 +3
공격력 높은 사람이 -1

비기면 둘다 +1
'''
import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = [[0,2], [3,-1]]

A_score = 0
B_score = 0

for i in range(N):
	if A[i] == B[i]:
		A_score += 1
		B_score += 1
	else:
		# B가 이기면 c = 1
		c = A[i] < B[i]
		# 차이가 7이면 is_seven = 1
		is_seven = abs(A[i]-B[i]) == 7
		A_score = A_score + d[is_seven][c^1]
		B_score = B_score + d[is_seven][c]
		
print(A_score, B_score)
		
	











