from collections import deque       
def solution(board):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    dist = [[0]*7 for _ in range(7)]
    Q = deque()
    Q.append([0,0])
    board[0][0] = 1
    L = 0
    while Q:
        n = len(Q)
        for i in range(n):
            r, c = Q.popleft()
            # 4¹æÇâ Å½»ö
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < 7 and 0 <= nc < 7 and board[nr][nc] == 0:
                    board[nr][nc] = 1
                    dist[nr][nc] = L + 1
                    Q.append([nr, nc])
        L += 1

    return -1 if dist[6][6] == 0 else dist[6][6]
                    
            
print(solution([[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0]]))

