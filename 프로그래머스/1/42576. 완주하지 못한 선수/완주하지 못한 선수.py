
def solution(participant, completion):
    temp = 0
    dic = {}
    
    for p in participant:
        dic[hash(p)] = p
        temp += int(hash(p))
    for c in completion:
        temp -= int(hash(c))
        
    return dic[temp]