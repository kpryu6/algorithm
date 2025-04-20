'''
# 이분탐색
# 정렬되어 있는거로 함
import bisect

listA = [1,2,4,3,6,7,8,34]
listA.sort()
# 4가 시작되는 위치
print(bisect.bisect_left(listA,9))

# 4가 끝난 후의 위치
print(bisect.bisect_right(listA,-5) - 1)

# 리스트에 없는건데, 큰 수면 리스트 길이 출력
# 리스트에 없는건데, 작은 수면 0 출력
'''

'''
6 # 수열 길이
5 -7 6 9 0 -3
3 # 모니터 출력 수
9
-9
6
'''

import sys,bisect
input = sys.stdin.readline

N = int(input().rstrip())
li = list(map(int, input().split()))
li.sort()
M = int(input().rstrip())

for _ in range(M):
	B = int(input().rstrip())
	idx = bisect.bisect_left(li,B)
	
	if idx < N and li[idx] == B:
		print(1)
	else:
		print(0)
