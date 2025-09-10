'''
1: 12345
2: 21232425
3: 3311224455

배열끼리 비교해서 같은거 세는거?
이중 for문은 안된다 다른방식으로 생각해보자 
인덱스? 인덱스같은데
'''
def solution(answers):
    answer = []
    c = [[i+1,0] for i in range(3)]
        
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == n1[i % len(n1)]:
            c[0][1] += 1
        if answers[i] == n2[i % len(n2)]:
            c[1][1] += 1
        if answers[i] == n3[i % len(n3)]:
            c[2][1] += 1

    # 값이 큰 순서대로 인덱스 정렬
    '''
    [3,4,5] -> [3]
    [1,3,3] -> [2,3]
    
    [(1,1), (2,3), (3,3)] -> key=lambda x: (x[0],-x[1]) -> [(2,3), (3,3), (1,2)]
    '''
    sorted_c = sorted(c, key=lambda x: (-x[1], x[0]))

    mx = sorted_c[0][1]
    
    for x in sorted_c:
        if x[1] == mx:
            answer.append(x[0])
        
    return answer