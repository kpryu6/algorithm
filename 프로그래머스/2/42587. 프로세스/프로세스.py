'''
특정 프로세스가 몇번째로 실행되는지?
a = Q.popleft()
if a = 우선순위 젤 높음:
    실행 후 종료
else:
    Q.append(a)
    
pri = 각 프로세스 우선순위
loc = 프로세스 위치 - 이 프로세스가 몇버째로 실행되는지 알고싶은것 (0~)

[0,1,2,3] - loc
[2,1,3,2] - pri

loc이랑 pri랑 묶어야함

[1,3,2,2] -> [3,2,2,1] -> 3 제거 [2,2,1] -> 2제거 [2,1] -> 2제거 [1] -> 1제거 []
'''
from collections import deque

def solution(pri, loc):
    answer = 0
    d = deque([(i,p) for (i,p) in enumerate(pri)])
    # print(d)
    
    while d:
        cur = d.popleft()
        if d and cur[1] < max(q[1] for q in d):
            d.append(cur)
        else:
            answer += 1
            if cur[0] == loc:
                return answer
    
'''
    li = []
    for idx,p in enumerate(pri):
        li.append((idx,p))
        
    max_pri = max(pri)

    deq = deque(li)
     
    # RuntimeError: deque mutated during iteration -> iteration 중에 deque 변경되어서 오류 ->
    그럼 하나씩 뺴야지 while로 가자
    for x in deq:
        if x[1] < max_pri:
            deq.popleft()
'''
        










