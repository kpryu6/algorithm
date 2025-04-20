def solution(board, k):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    n = len(board)
    r, c = 0, 0
    d = 1

    # ½Ã°£
    cnt = 0
    while cnt < k :
        cnt += 1
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
            r = nr
            c = nc
        else:
            d = (d + 1) % 4
    return [r, c]
        


print(solution([[0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0]], 10))

print(solution([[0, 0, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]], 20))

print(solution([[0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]], 25))
