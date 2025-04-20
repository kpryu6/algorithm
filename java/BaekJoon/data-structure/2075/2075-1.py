'''
1. heapq로 정렬해서 4개 빼면 되는거 아뇨?
'''
# import sys, heapq
# input = sys.stdin.readline
# 
# N = int(input().rstrip())
# q = []
# for _ in range(N):
#     num_list = list(map(int, input().rstrip().split()))
#     for num in num_list:
#         heapq.heappush(q, -num)
# for _ in range(N-1):
#     heapq.heappop(q)
# 
# print(-q[0])

# 위처럼 하면 시간초과 나옴 (N이 길어지기 때문이죠?)
# N을 고정해보자

import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())
q = []
for _ in range(N):
    num_list = list(map(int, input().rstrip().split()))
    if not q:
        for num in num_list:
            heapq.heappush(q, num)
    else:
        for num in num_list:
            if num > q[0]:
                heapq.heappop(q)
                heapq.heappush(q, num)
print(q[0])
