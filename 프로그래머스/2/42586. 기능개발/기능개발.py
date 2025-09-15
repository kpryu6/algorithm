'''
while True:
    cnt += 1
    for i in range(len(speeds)) 
        cnt += 1 -> 이러면 cnt가 3까지인데? 밖으로 나가야함
        cnt가 7일 때 93과 30이 나오는데
        93은 progresses[i] + speeds[i]*cnt가 100이 되었으니 나오는거고
        30도 progresses[i] + speeds[i]*cnt가 100 이상이니 나오는거임
'''

def solution(progresses, speeds):
    answer = []
    deploy = []
    # 먼저 배포까지 걸리는 시간 배열 만들기
    for pg, sp in zip(progresses,speeds):
        n = 0
        while pg < 100:
            pg += sp
            n += 1
        deploy.append(n)
    
    # print(deploy)
    # 배포 기준일
    standard = deploy[0]
    
    # 배포 가능 작업 수
    cnt = 1
    
    for i in range(1, len(deploy)):
        if deploy[i] <= standard:
            cnt += 1
        else:
            answer.append(cnt)
            standard = deploy[i]
            cnt = 1
    
    answer.append(cnt)
    
    
    # 흑역사
    # while True:
    #     cnt += 1
    #     deploy = 0
    #     # 아 이러면 answer에 담아도 계속 도는데.. 그럼 답이 이런식으로 나옴 [2,2,2,2,2,2,2,2,2.....3]
    #     for i in range(len(speeds)):
    #         if (progresses[i] + speeds[i]*cnt) >= 100:
    #             deploy += 1
    #             progresses.pop(i)
    #             speeds.pop(i)
    #     answer.append(deploy)
    return answer