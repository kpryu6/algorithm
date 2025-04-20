def solution(n,moves):
    r = c = 0
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    dir = {'U' : 0,'R' : 1,'D' : 2,'L' : 3}

    for command in moves:
        nr = r + dr[dir[command]]
        nc = c + dc[dir[command]]

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue

        r = nr
        c = nc

    return [r, c]
                            
print(solution(5, 'RRRDDDUUUUUUL'))
#print(solution(7, 'DDDRRRDDLL'))
#print(solution(5, 'RRRRRDDDDDU'))
#print(solution(6, 'RRRRDDDRRDDLLUU'))
