def solution(moves):
    r = c = 0
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    dir = ['U','R','D','L']

    for command in moves:
        for k in range(4):
            if command == dir[k]:
                r = r + dr[k]
                c = c + dc[k]
    return [r, c]
                            
print(solution('RRRDDDLU'))
#print(solution('DDDRRRDDLL'))
#print(solution('RRRRRRDDDDDDUULLL'))
#print(solution('RRRRDDDRRDDLLUU'))
