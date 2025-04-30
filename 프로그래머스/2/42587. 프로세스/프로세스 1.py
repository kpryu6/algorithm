'''
1. 일단 하나 꺼내기
2. 자기가 우선순위가 젤 안높으면 다시 넣기 (뒤로) rotate(1)
3. 자기가 우선순위가 젤 높으면 빼기

[A, B, C, D]
[2, 1, 3, 2]

[C, D, A, B]

# 우선순위 배열 -> properties
# 알고싶은 프로세스 위치 -> location

location 프로세스 몇번 째 실행됨?

-> 각 프로세스와 우선순위 묶기
(프로세스 위치, 우선순위)
[(0,2), (1,1), (2,3), (3,2)]

'''
def solution(priorities, location):
    from collections import deque
    d = deque([(i,p) for i,p in enumerate(priorities)])
    cnt = 0
    
    while d:
        # [(0,2), (1,1), (2,3), (3,2)]
        cur = d.popleft()
        # [0,2]
        # 우선순위가 자신이 젤 높지않으면:
        if any(cur[1] < q[1] for q in d):
            d.append(cur)
        # 젤 높거나 location과 같으면 return
        else:
            cnt += 1
            if cur[0] == location:
                return cnt

    
        
    
