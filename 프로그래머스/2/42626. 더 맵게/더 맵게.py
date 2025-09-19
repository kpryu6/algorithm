'''
스코빌 지수 낮은거 2개 섞어서 만듦

모든 음식 >= K 될때까지 반복해서 섞음

scovile = [2,3,4,5]

모든 음식의 스코빌 지수를 K 이상으로 -> 몇번?

[1,2,3,9,10,12]

1. 가장 낮은거 1, 2
1 + 2*2 = 5
[5,3,9,10,12]

2. 가장 낮은거 3,5
3 + 5*2 = 13
[13,9,10,12]
'''
import heapq

def solution(s, K):
    answer = 0
    heapq.heapify(s)
    while len(s) > 1 and s[0] < K:
        answer += 1
        a = heapq.heappop(s)
        b = heapq.heappop(s)
        heapq.heappush(s,a+(b*2))
    
    if s[0] < K:
        return -1
    return answer