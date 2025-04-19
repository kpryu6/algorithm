# K번째수 1.py 를 좀 더 간략히 표현한 것

def solution(array, commands):
    answer = []
    for cmd in commands:
        i,j,k = cmd
        answer.append(list(sorted(array[i-1:j]))[k-1])
        
    return answer
