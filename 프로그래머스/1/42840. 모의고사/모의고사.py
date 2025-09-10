# 첫 시도
def solution(answers):
    answer = []
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    
    # [[1, 1번수포자 정답개수],[2, 2번수포자 정답개수],[3, 3번수포자 정답개수]]
    c = [[i+1,0] for i in range(3)]
        
    # 각 수포자 정답개수 채우기
    for i in range(len(answers)):
        if answers[i] == n1[i % len(n1)]:
            c[0][1] += 1
        if answers[i] == n2[i % len(n2)]:
            c[1][1] += 1
        if answers[i] == n3[i % len(n3)]:
            c[2][1] += 1

    # 값이 큰 순서대로 인덱스 정렬
    sorted_c = sorted(c, key=lambda x: (-x[1], x[0]))

    # 가장 많이 맞춘 개수
    mx = sorted_c[0][1]
    
    # mx 넣기, mx랑 같은애들 넣기(현재 인덱스는 정렬되어있어서 그대로 넣으면 됨)
    for x in sorted_c:
        if x[1] == mx:
            answer.append(x[0])
        
    return answer
