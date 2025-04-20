'''
x가 자연수면,
배열에 x 추가

x가 0이면,
배열에서 가장 작은 값 출력하고 그 값 제거(pop)

입력에서 0이 주어진 횟수만큼 답을 출력한다

-> 우선순위 큐 사용하자

'''
import sys
import heapq
input = sys.stdin.readline
li = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num > 0:
        heapq.heappush(li, num)
    elif num == 0:
        if len(li) == 0:
            print(0)
        else:
            print(heapq.heappop(li))


