'''
begin -> target
한번에 1개의 알파벳만 변경
words 돌면서 해야됨 -> BFS 해야됨 최단거리라서

# 이거 아니에요
O(n^2) ??
hit에서 처음에 싹 봐야되는건가 그럼 갈 수 있는거들 인덱스에 +시간
시간 1 [1,0,0,0,0,0] -> hot -> [dot dog lot log cog]
시간 2 [1,2,0,2,0,0] -> dot lot [dog lot log cog]
시간 3 [1,3,3,3,0,0] -> dot lot dog [lot log cog]
시간 4 [4,4,4,4,4,4] -> 싹 됨 cog면 return

while 

if begin not in target:
    return 0
    
for x in words:
    if 1개의 단어만 다른지:
        begin = x
        cnt += 1
    else:
        continue

'''

# 단어 2개(x,y) 비교해서 문자 하나만 다른지 찾는 함수
def isdiff_one(x,y):
        x = list(x)
        y = list(y)
        cnt = 0
        
        for i in range(len(x)):
            if x[i] != y[i]:
                cnt += 1
                
        if cnt == 1:
            return True
        
        return False

from collections import deque

def solution(begin, target, words):
        
    if target not in words:
        return 0
    
    Q = deque([(begin,0)])
    # 이건 미쳤다
    visited = {begin}

    while Q:
        cur, cnt = Q.popleft()
        
        if cur == target:
            return cnt
        
        for nxt in words:
            # 다음 단어로 넘어가기
            if nxt not in visited and isdiff_one(cur,nxt):
                visited.add(nxt)
                Q.append([nxt,cnt+1])
        
        print("visited= ", visited)
        print("Q= ", Q)
    return 0
        
    return cnt