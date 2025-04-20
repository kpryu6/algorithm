from collections import deque
def solution(home):
    check = [0] * 10000
    Q = deque()
    Q.append(0)
    L = 0
    check[0] = 1
    while Q:
        n = len(Q)
        for i in range(n):
            v = Q.popleft()
            for nv in [v-1, v+1, v+5]:
                if nv == home:
                    return L + 1
                if nv >=0 and nv <= 10000 and check[nv] == 0:
                    Q.append(nv)
                    check[nv] = 1

        L += 1

    
            
print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))
