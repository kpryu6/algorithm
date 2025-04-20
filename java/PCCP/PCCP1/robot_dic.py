def solution(moves):
    r = c = 0
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    dir = {'U' : 0,'R' : 1,'D' : 2,'L' : 3}

    for command in moves:
        r = r + dr[dir[command]]
        c = c + dc[dir[command]]
    return [r, c]
                            
print(solution('RRRDDDLU'))
#print(solution('DDDRRRDDLL'))
#print(solution('RRRRRRDDDDDDUULLL'))
#print(solution('RRRRDDDRRDDLLUU'))
