'''
A-B
B-C

A-C

연결된 무리 개수 구하는거

방문 여부 -> 방문 안됐다? -> 네트워크 개수 증가 -> 방문 -> 방문여부 체크 -> 이웃 체크 -> 방문 안된것들 싹 연결(dfs) -> 끝
'''

def solution(n, computers):
    answer = 0
    # n개 컴퓨터의 방문 여부
    visited = [False] * n
    
    def dfs(computer_idx):
        visited[computer_idx] = True
        
        for neighbor_idx in range(n):
            # 연결 & 방문X 이면
            if computers[computer_idx][neighbor_idx] == 1 and not visited[neighbor_idx]:
                dfs(neighbor_idx)
            
        
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
            

    return answer