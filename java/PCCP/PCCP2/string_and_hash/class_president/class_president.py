from collections import defaultdict, Counter


def solution(s):
    answer = ""
    sH = defaultdict(int)
    # 빈도수 카운팅
    for x in s:
        sH[x] += 1

    maxC = 0
    for key in sH:
        if sH[key] > maxC:
            maxC = sH[key]
            answer = key

    return answer


print(solution("BACBACCACCBDEDE"))
# print(solution("AAAAABBCCDDDD"))
# print(solution("AABBCCDDEEABCB"))
