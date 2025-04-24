'''
논문 n편 중
h번 이상 인용된 논문 -> h편 이상
h번 이하 인용된 논문 -> 나머지

--> h의 최댓값
'''
def solution(citations):
    citations.sort(reverse=True)
    
    for i, cite in enumerate(citations):
        print("idx: ", i+1, "cite: ", cite)
        if i+1 > cite:
            return i
    
    # 예외처리
    if citations[-1] > len(citations):
        return len(citations)
    
        
        
    return answer