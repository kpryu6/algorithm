'''
비교를 어떤 방식으로 할 것인가

'''
def solution(phone_book):
    phone_book.sort()
    
    for a,b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
        
    return True
        