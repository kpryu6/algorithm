'''
(1,1)에서 (5,5)까지 가는거
BFS구나
경로를 나타내는 지도 만두야지 = counters

(5,5) 부분에 경우의 수가 그대로면 -1 return

        m
    ㅡㅡㅡㅡㅡ
    |
n   |
    |
'''
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])

    Q = deque([(0,0)])
    
    # 남 북 동 서
    # xy 그래프 시계방향으로 90도 회전
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while Q:
        x,y = Q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 벗어나거나 벽이면
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 0:
                continue
            
            # 아직 방문하지 않았으면
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                # 현재 위치 추가
                Q.append((nx,ny))
        
    answer = maps[n-1][m-1]
        
    return answer if answer > 1 else -1