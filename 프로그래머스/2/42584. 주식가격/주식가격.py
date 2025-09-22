'''
prices: 주식가격들 (초단위))
가격 안떨어진 기간?

완전탐색?
1초 = 끝까지 가격 안떨어짐 -> 4
2초 = -- -> 3
3초 = 1초 뒤 떨어짐 -> 1
4초 = 안떨어짐 -> 1
5초 -> 안떨어짐 -> 0


3초때는 3초를 세서 1인데 왜 나머지는 해당 초를 안셈?
'''
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        cnt = 0
        cur = prices.popleft()
        for p in prices:
            if cur > p:
                cnt += 1
                break
            
            cnt += 1
        answer.append(cnt)
    
    return answer