def solution(s):
    stack = []
    for c in s:
        # 1. ')'가 나왔을때
        # - stack에 '(' 가 있으면 '(' pop
        # - 없으면 append
        if c == ')':
            if '(' in stack:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    
    if len(stack) == 0:
        return True
    else:
        return False
        
        
