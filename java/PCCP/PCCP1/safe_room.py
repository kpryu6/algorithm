def solution(board):
    answer = 0
    n = len(board)

    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]
    for i in range(n):
        for j in range(n):
            flag = True
            if board[i][j] == 1:
                continue
            for k in range(8):
                ii = i + dr[k]
                jj = j + dc[k]
                if 0 <= ii < n and 0 <= jj < n and board[ii][jj] == 1:
                    flag = False
                    break
            if flag:
                answer += 1
    return answer
                