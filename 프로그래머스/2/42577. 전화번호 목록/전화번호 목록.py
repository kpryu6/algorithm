# 접두사를 어떻게 찾지?
# 개수X 순서까지 똑같아야함
# 번호끼리의 비교를 어떻게 할까? 비교 비교 비교
# 


def solution(phone_book):
    phone_book.sort()
    
    # phone_book -> ["123","456","789"]
    # phone_book[1:] -> ["456", "789"]
    # 하나씩 밀리니까 됨
    for a,b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    
    return True
    