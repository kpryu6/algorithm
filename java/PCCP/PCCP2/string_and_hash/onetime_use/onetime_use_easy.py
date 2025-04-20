from collections import defaultdict, Counter


def solution(s):
    answer = 1e9
    sH = Counter(s)

    for i in range(len(s)):
        if sH[s[i]] == 1:
            return i + 1

    if answer == 1e9:
        answer = -1

    return answer


print(solution("statitsics"))
print(solution("aabb"))
print(solution("stringshowtime"))
print(solution("abcdeabcdfg"))
