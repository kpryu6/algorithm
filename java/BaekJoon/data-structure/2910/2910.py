'''

'''
n, c = map(int, input().split())
_list = list(map(int, input().split()))
# 빈도
cnt = {}
# 우선순위
idx = 1

for num in _list:
    if num in cnt:
        cnt[num][0] += 1
    else:
        cnt[num] = [1, idx]
        idx += 1
# print(cnt)

numbers = [[i,j] for i, j in cnt.items()]
# print(numbers)
# 빈도수는 내림차순, 우선순위는 오름차순으로
numbers.sort(key=lambda x:(-x[1][0], x[1][1]))

# print(numbers)

res = []
for i, j in numbers:
    res += [i]*j[0]

# print(res)

print(*res)
