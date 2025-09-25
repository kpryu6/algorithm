'''
begin에서 target으로 가는데
words에 target이 있다아임니까

words 싹 뒤지면서 
begin이랑 비교하면서
words에 있는 애들 거리 추가해서 ㄱㄱ (dog, 4) 요런식으로


'''
from collections import deque

# cur이랑 하나만 다른애들 yield
def get_adjacent(cur,words):
    
    # 음 이거 O(n^2)이라 별로인것같은데; 그치
    for word in words:
        cnt = 0
        for c,w in zip(cur,word):
            if c != w:
                cnt += 1
        
        if cnt == 1:
            yield word
    
def solution(begin, target, words):
    # 예외처리1
    if target not in words:
        return 0
    
    Q = deque([begin])
    dist = {begin: 0}
    
    while Q:
        cur = Q.popleft()
        
        # 뽑은거랑 조건에 맞는 next_word랑 비교해야지
        for next_word in get_adjacent(cur,words):
            if next_word not in dist:
                dist[next_word] = dist[cur] + 1
                Q.append(next_word)
    
    return dist.get(target,0)
            