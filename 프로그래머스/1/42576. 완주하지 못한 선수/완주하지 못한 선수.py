
from collections import Counter

def solution(participant, completion):
    counter_part = Counter(participant)
    counter_comp = Counter(completion)
    
    answer = counter_part - counter_comp
    
    return list(answer.keys())[0]