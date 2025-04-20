tmp = []
def DFS(L, n, m):
    if L == m:
        for x in tmp:
            print(x, end = ' ')
        print()
    else:
        for i in range(1, n+1):
            tmp.append(i)
            DFS(L + 1, n, m)
            tmp.pop()
            

def solution(n, m):         
    DFS(0, n, m)

                                       
solution(3, 2)
