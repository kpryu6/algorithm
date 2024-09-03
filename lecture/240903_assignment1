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
# 각 리스트를 만들어서 인덱스끼리 비교해보자.
import sys
input = sys.stdin.readline

N = int(input().rstrip())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_score = 0
B_score = 0

for i in range(N):
	if A[i] > B[i]:
		if A[i] - B[i] == 7:
			A_score += -1
			B_score += 3
		else:
			A_score += 2
	elif A[i] < B[i]:
		if B[i] - A[i] == 7:
			B_score += -1
			A_score += 3
		else:
			B_score += 2
	elif A[i] == B[i]:
		A_score += 1
		B_score += 1

print(A_score, B_score)
		
	










