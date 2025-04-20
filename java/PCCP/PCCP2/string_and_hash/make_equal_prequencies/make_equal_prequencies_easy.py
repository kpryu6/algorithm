from collections import defaultdict, Counter


def solution(s):

    answer = []
    cnt = Counter(s)
    max_cnt = max(cnt.values())
    for ch in ['a', 'b', 'c', 'd', 'e']:
        answer.append(max_cnt - cnt[ch])
    return answer


print(solution("aaabc"))
print(solution("aabb"))
print(solution("abcde"))
print(solution("abcdeabc"))
print(solution("abbccddee"))
