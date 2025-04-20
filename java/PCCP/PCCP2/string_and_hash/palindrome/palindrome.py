from collections import Counter


def solution(s):
    answer = 0
    sH = Counter(s)
    use = False
    for i in sH:
        if (sH[i] % 2) == 0:
            answer += sH[i]
        elif (sH[i] % 2) == 1 and use == False:
            answer += sH[i]
            use = True
        else:
            answer += sH[i] - 1
    return answer


print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))
