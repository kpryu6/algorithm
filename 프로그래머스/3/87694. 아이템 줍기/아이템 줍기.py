'''
둘레 따라서 이동
캐릭터 -> 아이템
begin -> target
가장 짧은 거리 BFS??????

테두리를 어떻게 이동하지? BFS로 그래프탐색처럼 하려면 어떻게?
'''
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 맵 2배 확대 및 초기화 (좌표 50까지라서 102 x 102)
    # 0: 빈공간, 1: 테두리, -1: 채워진 공간
    board = [[-1] * 102 for _ in range(102)]
    
    # 직사각형 테두리 그리기
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # 모든 사각형의 내부를 0으로 채움
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if board[i][j] != 0:
                    # 테두리는 1 *************
                    if i == x1 or i == x2 or j == y1 or j == y2:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
    
    # BFS로 최단거리 탐색
    cx, cy = characterX*2, characterY*2
    ix ,iy = itemX*2, itemY*2
    
    # 출발
    q = deque([(cx,cy)])
    visited = [[0]*102 for _ in range(102)]
    visited[cx][cy] = 1
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while q:
        x,y = q.popleft()
        
        if x == ix and y == iy:
            return (visited[x][y] - 1) // 2
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위 안 & 방문하지 않았 & 테두리
            if 0 <= nx < 102 and 0 <= ny < 102 and visited[nx][ny] == 0 and board[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    