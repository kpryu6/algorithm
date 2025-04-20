from collections import defaultdict


def solution(s):
    answer = 0
    sH = defaultdict(int)
    ch = None
    for x in s:
        sH[x] += 1
    for x in sH:
        if sH[x] == 1:
            ch = x
            break
    if ch is not None:
        answer = s.index(ch) + 1
    else:
        answer = -1  # 유일한 문자가 없는 경우 -1로 처리

    return answer


print(solution("statitsics"))
print(solution("aabb"))
print(solution("stringshowtime"))
print(solution("abcdeabcdfg"))
