def solution(moves):
    r = c = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    d = 1
    for command in moves:
        if command == 'G':
            r = r + dr[d]
            c = c + dc[d]
            # 방향은 유지하면서 후진하고 싶으면
            # r = r - dr[d]
            # c = c - dc[d]
        elif command == 'R':
            # 시계 방향으로 90도 회전
            d = (d + 1) % 4
        elif command == 'L':
            # 시계 방향으로 270도 회전
            d = (d + 3) % 4


    return [r, c]


print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))
