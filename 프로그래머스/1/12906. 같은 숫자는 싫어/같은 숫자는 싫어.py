def solution(arr):
    answer = []
    for x in arr:
        if len(answer) == 0:
            answer.append(x)
        if x == answer[-1]:
            continue
        answer.append(x)
    return answer