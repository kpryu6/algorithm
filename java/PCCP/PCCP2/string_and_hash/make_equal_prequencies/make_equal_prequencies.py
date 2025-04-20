from collections import defaultdict


def solution(s):

    answer = []
    max_value = 0

    sH = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

    for x in s:
        sH[x] += 1

    for key in sH:
        max_value = max(max_value, sH[key])

    for key in sH:
        answer.append(max_value - sH[key])

    return answer


print(solution("aaabc"))
print(solution("aabb"))
print(solution("abcde"))
print(solution("abcdeabc"))
print(solution("abbccddee"))
