'''
왼쪽부터 정렬, 오른쪽부터 정렬해서(그냥 정렬말고)

높이를 싹 더하면됨
'''
import sys
input = sys.stdin.readline

N = int(input().rstrip())
li = [list(map(int, input().rstrip().split())) for _ in range(N)]
li.sort()
# print(li)
# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]

# 왼쪽부터 현재 높이 최대값을 저장
idx = 0
cur_height = 0
height_li = [0 for _ in range(li[-1][0]+1)]
for i in range(li[0][0], li[-1][0]+1):
    # 초기값
    if idx == 0:
        cur_height = li[0][1]
        idx += 1
    else:
        if li[idx][0] == i:
            if cur_height < li[idx][1]:
                cur_height = li[idx][1]
            idx += 1

    height_li[i] = cur_height

# print(height_li)
# [0, 0, 4, 4, 6, 6, 6, 6, 10, 10, 10, 10, 10, 10, 10, 10]

# 오른쪽부터 현재 높이 최대값을 저장
idx = N - 1
cur_height = 0
for i in range(li[-1][0], li[0][0]-1, -1):
    if idx == N-1:
        cur_height = li[-1][1]
        idx -= 1
    else:
        if li[idx][0] == i:
            if cur_height < li[idx][1]:
                cur_height = li[idx][1]
            idx -= 1
    height_li[i] = min(height_li[i], cur_height)
print(sum(height_li))
