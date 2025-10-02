'''
4C2
최대한 많은 종류 폰켓몬 N/2마리 선택

1번

2번 
1. 일단 6/2 -> 3
2. 여기 key 개수
    3: 3개
    2: 2개
    4: 1개
1번과 2번 개수 중 작은거

3번
1. 일단 6/2 -> 3

3: 3개
2: 3개
'''
def solution(nums):
    return min(len(nums)/2,len(set(nums)))
    