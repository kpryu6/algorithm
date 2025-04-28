'''
개발속도 다름
앞에 있는 기능이 배포될때 뒤에꺼도 같이 배포

progresses = (먼저 배포되어야 햐는 순서) 작업의 진도
speeds = 각 작업의 개발 속도

각 배포마다 몇개의 기능이 배포되는지 return

앞에꺼가 배포가 될 수 있어야 뒤에꺼도 같이 배포됨 -> 뒤에꺼는 작업 다 되었어도 기다려야됨

1. [7, 4, 9] -> 하나씩 뽑는데, 7보다 작은거 싹 뽑고 개수 세고, 그다음꺼 이렇게 -> [2,1]
2. [5, 10, 1, 1, 20, 1] -> [1, 3, 2]
'''
def solution(progresses, speeds):
    answer = []
    comp = []
    for pg, sp in zip(progresses, speeds):
        n = 0
        while pg < 100:
            pg += sp
            n += 1
        comp.append(n)
    # print(comp)
    
    # 처음 배포 기준일
    standard = comp[0]
    # 배포 가능한 작업 수
    cnt = 1
    
    # 리스트에서 빼는데, 앞의 값보다 작은 값까지 다 빼고 answer에 개수 넣고 반복.
    for i in range(1, len(comp)):
        if comp[i] <= standard:
            cnt += 1
        else:
            answer.append(cnt)
            standard = comp[i]
            cnt = 1
    
    answer.append(cnt)
            
    
    return answer
