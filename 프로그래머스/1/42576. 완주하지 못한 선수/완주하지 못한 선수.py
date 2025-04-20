'''
한명빼고 모두 완주
participant - completion

Counter로 세어보자
'''

def solution(participant, completion):
    from collections import Counter
    p = Counter(participant)
    c = Counter(completion)
    a = list(p - c)
    
    return a[0]
    