import heapq 

def solution(s, K):
    answer = 0
    heapq.heapify(s)
    
    while s and s[0] < K:
        try:
            new = heapq.heappop(s) + heapq.heappop(s)*2
            heapq.heappush(s,new)
            answer += 1
        except:
            return -1
    return answer