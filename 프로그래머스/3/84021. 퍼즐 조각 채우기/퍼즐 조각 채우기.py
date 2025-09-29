'''
퍼즐 조각 -> 게임보드에 놓기
정사각형!
game_board = 게임보드 상태
table = 퍼즐 조각 상태

최대한 많이 채우기 -> 최대 몇칸?

감도안옴 길찾기?는 아니고
일단 회전 가능
조각을 따로 분리?

최대범위?
1번 -> + 모양
2번 -> 3 x 3
3번 -> 2 x 2
4번 -> 2 x 2
5번 -> 2 x 2

다 안넣어도 됨 근데 최대로 채워야함

넣는걸 어떻게 표현?
퍼즐 조각 각각을 독립적으로 어떻게 표현? -> 정규화? 어떻게?

정규화해서
보드에 0인부분에서 하나씩 가져와서 비교
딱맞으면 answer +=


'''
from collections import deque

# BFS로 연결된 Block 찾는 함수
def find_blocks(board, value):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    blocks = []
    
    # board 뒤져서 block 생성 후 blocks에 넣기
    for r in range(n):
        for c in range(n):
            if board[r][c] == value and not visited[r][c]:
                q = deque([(r,c)])
                visited[r][c] = True
                block = [(r,c)]
                
                dx = [-1,1,0,0]
                dy = [0,0,-1,1]
                
                # r,c에 대해 bfs로 block 잇기
                while q:
                    br, bc = q.popleft()
                    for dr, dc in zip(dx,dy):
                        nr, nc = br+dr, bc+dc
                        if 0 <= nr < n and 0 <= nc < n and \
                        board[nr][nc] == value and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                            block.append((nr,nc))
                            
                blocks.append(block)
    return blocks

# block을 (0,0) 기준으로 정규화하는 함수
def normalize(block):
    min_x = min(x for x,y in block)
    min_y = min(y for x,y in block)
    return sorted([(x-min_x,y-min_y) for x,y in block])
    
# block을 90도로 회전시키는 함수
def rotate_90(block):
    # (2,-3)일 시 (-3,-2)
    rotated = [(c,-r) for r,c in block]
    return normalize(rotated)

def solution(game_board, table):
    answer = 0
    
    # 게임보드 빈 공간(0) 정규화
    empty_spaces = [normalize(block) for block in find_blocks(game_board, 0)]
    # 퍼즐 조각(1) 정규화
    puzzle_pieces = [normalize(block) for block in find_blocks(table, 1)]
    
    print(empty_spaces)
    print(puzzle_pieces)
    
    puzzle_used = [False] * len(puzzle_pieces)
    
    # 조각 맞추기
    for space in empty_spaces:
        is_matched = False
        for i in range(len(puzzle_pieces)):
            if puzzle_used[i]:
                continue
            
            cur = puzzle_pieces[i]
            
            # 4번 회전하며 비교
            for _ in range(4):
                if space == cur:
                    answer += len(space)
                    puzzle_used[i] = True
                    is_matched = True
                    break
                cur = rotate_90(cur)
            
            # puzzle_pieces[i] 맞춰지면 끝내기 -> 1번 for문으로 다음 space
            if is_matched:
                break
    
    return answer





