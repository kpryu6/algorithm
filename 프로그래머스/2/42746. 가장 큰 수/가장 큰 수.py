'''
정렬을 어떻게 할지?
문자열로 바꿔?
'''

def solution(numbers):
    from functools import cmp_to_key
    
    # 하나씩 비교
    def compare(x,y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    str_numbers = list(map(str,numbers))
    str_numbers.sort(key=cmp_to_key(compare))
    
    # 예외처리!!!!!!!!!! 이거 안해서 틀림 계속
    # 가장 큰 게 맨 앞인데, 0이면 다 0 이니까
    if str_numbers[0] == '0':
        return '0'
    
    return "".join(str_numbers)