'''
1명 빼고 완주

그 1명 return
'''
def solution(participant, completion):
    
    temp = 0
    dict = {}
    
    for p in participant:
        # p를 출력해야 하니깐 hash를 키로
        dict[hash(p)] = p
        temp += hash(p)
    
    for c in completion:
        temp -= hash(c)
    
    return dict[temp]