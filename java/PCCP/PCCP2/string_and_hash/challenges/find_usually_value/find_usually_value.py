from collections import Counter


def solution(array):
    answer = []
    iH = Counter(array)
    maxC = 0
    for key in iH:
        if iH[key] > maxC:
            maxC = iH[key]
    for key in iH:
        if iH[key] == maxC:
            answer.append(key)

    return -1 if len(answer) > 1 else answer[0]
