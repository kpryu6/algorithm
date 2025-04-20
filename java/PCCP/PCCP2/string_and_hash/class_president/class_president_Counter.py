from collections import defaultdict, Counter


def solution(s):
    answer = ""
    # 빈도수 카운팅
    sH = Counter(s)
    maxC = 0
    for key in sH:
        if sH[key] > maxC:
            maxC = sH[key]
            answer = key

    return answer


print(solution("BACBACCACCBDEDE"))
# print(solution("AAAAABBCCDDDD"))
# print(solution("AABBCCDDEEABCB"))
