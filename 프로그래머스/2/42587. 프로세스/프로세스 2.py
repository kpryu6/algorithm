def solution(priorities, location):
    from collections import deque
    d = deque([(i,p) for i,p in enumerate(priorities)])
    cnt = 0
    
    while d:
        cur = d.popleft()
        # max 이용
        if d and cur[1] < max(q[1] for q in d):
            d.append(cur)
        else:
            cnt += 1
            if cur[0] == location:
                return cnt
