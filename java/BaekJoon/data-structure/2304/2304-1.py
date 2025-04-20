'''
왼쪽에서부터 x좌표로 정렬

왼쪽에서부터 높이 비교하면서 올라가기

오른쪽에서부터 높이 비교하면서 올라가기 (가운데가 10)

'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
height_arr = [0 for _ in range(arr[-1][0]+1)]

idx = 0
cur_height = 0
for i in range(arr[0][0], arr[-1][0]+1):
    # 초기값
    if idx == 0:
        cur_height = arr[0][1]
        idx += 1
    else:
        if arr[idx][0] == i:
            if cur_height < arr[idx][1]:
                cur_height = arr[idx][1]
            idx += 1
    
    height_arr[i] = cur_height
# print(height_arr)
idx = N-1
cur_height = 0
for i in range(arr[-1][0], arr[0][0]-1, -1):
    if idx == N-1:
        cur_height = arr[-1][1]
        idx -= 1
    else:
        if arr[idx][0] == i:
            if cur_height < arr[idx][1]:
                cur_height = arr[idx][1]
            idx -= 1
    height_arr[i] = min(height_arr[i], cur_height)
# print(height_arr)
print(sum(height_arr))
