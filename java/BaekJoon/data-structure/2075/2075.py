'''
모든 수는 자신의 한칸 위에 있는 수보다 큼
N번째 큰 수?


'''
import sys, heapq
input = sys.stdin.readline

N = int(input())
li = []
for i in range(N):
    _list = list(map(int, input().rstrip().split()))
    if not li:
        for num in _list:
            heapq.heappush(li, num) # min_heap 구조로 li 채우기
    else:
        for num in _list: # N 크기로 유지됨
            if li[0] < num:
                heapq.heappush(li, num) # num push
                heapq.heappop(li) # li[0] pop
print(li[0])
