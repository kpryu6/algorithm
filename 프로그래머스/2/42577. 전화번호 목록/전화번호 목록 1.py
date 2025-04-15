# 정렬 -> zip으로 묶어서 비교 -> startswith 함수사용


def solution(phone_book):
    phone_book.sort()
    
    # phone_book -> ["123","456","789"]
    # phone_book[1:] -> ["456", "789"]
    # 하나씩 밀리니까 됨
    for a,b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    
    return True
    
