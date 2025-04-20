from collections import defaultdict


def solution(name, yearning, photo):
    answer = []
    sH = defaultdict(int)
    for i in range(len(name)):
        sH[name[i]] = yearning[i]

    for x in photo:
        sum = 0
        for i in x:
            sum += sH[i]
        answer.append(sum)

    return answer
