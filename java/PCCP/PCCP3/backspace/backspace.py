def solution(s):
    answer = ""
    stack = []
    for x in s:
        if x == '#':
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(x)
    answer = answer.join(stack)

    return answer


print(solution("abc##ec#ab"))
print(solution("kefd#ef##s##"))
print(solution("teac#cher##er"))
print(solution("englitk##shabcde##ff##ef##ashe####"))
print(solution("itistime####gold"))
