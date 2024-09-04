import sys
input = sys.stdin.readline

table = dict()
N = int(input().rstrip())

# 딕셔너리에 저장
for i in range(N):
	item, price = map(str, input().split())
	price = int(price)
	table[item] = price

# max 출력
for key, val in table.items():
	if val == max(table.values()):
		print(key, val)

# min 출력
for key, val in table.items():
	if val == min(table.values()):
		print(key, val)
		
# 참고
'''
max(table,key=table.get)
table.get으로 value를 얻어 가장 큰 value를 가진 key 추출
'''
