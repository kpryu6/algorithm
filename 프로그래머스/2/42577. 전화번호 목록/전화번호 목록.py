'''
1개라도 접두어면 retuh
'''

def solution(phone_book):
    answer = True
    
    p = sorted(phone_book)

    for a,b in zip(p, p[1:]):
        if a == b[:len(a)]:
            answer = False
        
    return answer