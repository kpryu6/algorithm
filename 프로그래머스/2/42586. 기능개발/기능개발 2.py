def solution(pro, sp):
    Q = []
    for p, s in zip(pro,sp):
        # 개발 완료 기간
        complete = -((p-100)//s)
        
        # 처음에 아무것도 없으면 넣어주기
        # 아직 완료되지 않은 태스크 넣어주기
        if len(Q) == 0 or Q[-1][0] < complete:
            Q.append([complete,1])
        else:
            Q[-1][1] += 1
        
    return [q[1] for q in Q]
    # print(70//30) -> 2
    # print(-(-70//30)) -> 3
