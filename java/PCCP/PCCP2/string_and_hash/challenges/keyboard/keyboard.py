from collections import defaultdict


def solution(keymap, targets):
    answer = []
    sH = defaultdict(int)
    # keymap에 있는 각 문자 번호 매기기
    for x in keymap:
        for i in range(len(x)):
            if x[i] in sH:
                if i+1 < sH[x[i]]:
                    sH[x[i]] = i+1
            else:
                sH[x[i]] = i+1

    for x in targets:
        score = 0
        for y in x:
            if y in sH:
                score += sH[y]
            else:
                score = -1
                break
        answer.append(score)

    return answer
