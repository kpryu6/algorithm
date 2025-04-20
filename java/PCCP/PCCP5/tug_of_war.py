def DFS(L,p,ch, graph):
    if L == 7:
        for x in p:
            print(x, end =' ')
        print()
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                p.append(i)
                DFS(L+1, n, m, p,ch)
                # 백트래킹
                ch[i] = 0
                p.pop()





def solution(fight):
    answer  = 0
    graph = [[0]*8 for _ in range(8)]
    # 싸우는 애들 체크
    for a,b in fight:
        graph[a][b] = 1
        graph[b][a] = 1

    ch  = [0] * 8
    DFS(0, [])
         
    
    return answer

print(solution([[1, 3], [5, 7], [4, 2]]))
#print(solution([[3, 2], [3, 5], [5, 2], [7, 3]]))
#print(solution([[1, 2], [1, 5], [1, 7], [1, 3]]))
#print(solution([[1, 7]]))
#print(solution([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
