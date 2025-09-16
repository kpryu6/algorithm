'''
(시작 )끝
일단 하나하나씩 뽑아야할거 아님?
(로 시작하면 )로 끝나야함 
'''


def solution(s):
    answer = True
    store = []
    # print(s)
    for x in s:
        if x == '(':
            store.append(x)
        else:
            if '(' in store:
                store.pop()
            else:
                store.append(x)
                
    if len(store) > 0:
        return False
    
    return True