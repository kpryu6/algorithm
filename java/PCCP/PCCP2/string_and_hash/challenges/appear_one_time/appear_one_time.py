from collections import defaultdict


def solution(s):
    answer = []
    sH = defaultdict(int)

    for x in s:
        sH[x] += 1

    for key in sH:
        if sH[key] == 1:
            answer.append(key)

    # 배열에 있는거 str로 join
    return "".join(sorted(answer))
