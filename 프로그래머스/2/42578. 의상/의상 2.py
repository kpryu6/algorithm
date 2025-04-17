def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    # 예) cnt.values -> [2,1]
    # ((1*(2+1))*(1+1)) = 6
    # reduce(함수, iterable, 초기값)
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
