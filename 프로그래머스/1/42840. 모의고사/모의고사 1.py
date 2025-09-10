def solution(answers):
    answer = []
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    
    # [[1, 1번수포자 정답개수],[2, 2번수포자 정답개수],[3, 3번수포자 정답개수]]
    c = [0,0,0]
        
    # 각 수포자 정답개수 채우기
    for i in range(len(answers)):
        if answers[i] == n1[i % len(n1)]:
            c[0] += 1
        if answers[i] == n2[i % len(n2)]:
            c[1] += 1
        if answers[i] == n3[i % len(n3)]:
            c[2] += 1
    
    # enumerate로 index 생성
    for idx, s in enumerate(c):
        if s == max(c):
            answer.append(idx+1)
        
    return answer
