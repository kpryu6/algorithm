'''
[9,8,6,5,3,2,1] -> 4
논문 n편 중 h번 이상 인용된 논문이 h편 이상, 
-> index로 접근? 

나머지 논문이 h번 이하 인용
-> 남은 인용 횟수들이 index보다 작으면 됨 -> 걍 다음 인용 횟수가 index 이하면 됨
'''

def solution(citations):
    citations.sort(reverse=True)
    for i, cite in enumerate(citations):
        if cite < i + 1:
            return i
    return len(citations)

            
            
        
        
        
        
        