'''
# 조건부정렬 : 나만의 정렬
li = [3, 1, -5, 4, -10]

# 객체 정렬(여기선 2차원 배열 정렬)
li2 = [[1,3], [2,4], [3,3], [4,4], [5,5]]

# lambda로 무명함수 선언
squared_li = list(map(lambda x:x**2, li))
print(squared_li)

# 우선순위 만들 때 많이 사용
# 절댓값이 오름차순으로 되도록
li.sort(key = lambda x : abs(x))

# 절댓값 reverse
li.sort(key = lambda x : abs(x), reverse = True)
print(li)

# 다른 방법
li.sort(key = lambda x : -abs(x))
print(li)

# 배열의 2번째 값이 작을수록 우선순위 높도록
# 값이 같다면 1번째 값을 기준으로 우선순위
# 첫번째 우선순위 : 2번째 값이 작을수록
# 두번째 우선순위 : 1번째 값이 클수록
# x는 [1,3]들어오고, 그다음 [2,4] 들어오고 ...
li2.sort(key = lambda x : (x[1], -x[0]))
print(li2)

# 10에 가까울수록 우선순위
li.sort(key = lambda x : abs(x-10))
print(li)

'''

'''
5 섬의개수
0 0 
0 -2
-1 -1
-5 0
-1 10
'''

import sys
input = sys.stdin.readline

N = int(input().rstrip())
li = []

for i in range(N):
	x, y = map(int, input().split())
	li.append([x,y,i]) # 특정 섬이 어떤 섬인지 알려고 인덱스 붙여줌
'''
0 0 0
0 -2 1
-1 -1 2
-5 0 3
-1 10 4
'''
li.sort(key = lambda x : (-x[0], -x[1]))
'''
0 0 0
0 -2 1
-1 10 4
-1 -1 2
-5 0 3
'''
print(li)
res = [0] * N
cnt = 0 # 침략가능한 섬 개수

for i in range(N):
	res[li[i][2]] = cnt # 해당 섬의 인덱스에 cnt 추가
	cnt += 1

'''
res[0] = 0
res[1] = 1
res[4] = 2
res[2] = 3
res[3] = 4
'''
print(res)
for i in res:
	print(i)
	


