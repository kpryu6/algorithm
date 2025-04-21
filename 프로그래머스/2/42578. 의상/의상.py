def solution(clothes):
    clothes_type = {}
    cnt = 1
    
    for c,t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1
    
    for n in clothes_type.values():
        cnt *= n
    
    return cnt - 1
        