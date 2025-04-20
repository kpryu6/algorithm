'''
5 2 # N, C
2 1 2 1 2
-> 2 2 2 1 1

9 77
11 33 11 77 54 11 25 25 33
-> 11 11 11 33 33 25 25 77 54

각 숫자의 빈도를 저장해야함. 
(11, 3) 이런식으로 저장하고 뒤에것으로 정렬해보자.
'''
import sys
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))

# 빈도 수
cnt = {}
# 우선순위
pri = 1

# cnt[숫자] = [빈도수, 우선순위]

# 빈도 수 넣기
for num in li:
    if num in cnt:
        cnt[num][0] += 1
    # 처음  
    else:
        cnt[num] = [1, pri]
        pri += 1

num_list = [[i,j] for i,j in cnt.items()]

# 빈도 수는 내림차순, 우선순위는 오름차순으로 정렬
num_list.sort(key=lambda x: (-x[1][0], x[1][1]))

# for num, config in num_list:
#     vindo = config[0]
#     for _ in range(vindo):
#         print(num, end=" ")
res = []
for i, j in num_list:
    res += [i]*j[0]

# print(res)

print(*res)
