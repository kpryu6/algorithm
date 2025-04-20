def DFS(L, n, m, p, ch):
    # Level은 인덱스
    # 중복하면 안되니까 ch로 상태체크
    if L == m:
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




def solution(n,m):
    ch = [0] * (n+1)
    DFS(0, n, m, [], ch)

solution(5,4)