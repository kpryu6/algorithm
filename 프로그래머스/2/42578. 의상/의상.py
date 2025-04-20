'''

'''
def solution(clothes):
    answer = 1
    from collections import Counter
    c = Counter()
    for cloth in clothes:
        c[cloth[1]] += 1
    
    c_list = list(c.values())
    for i in range(len(c_list)):
        answer *= c_list[i]+1
    return answer -1
        
    
    