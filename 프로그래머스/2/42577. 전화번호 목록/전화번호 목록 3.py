# Set으로 풀어보자

def solution(phone_book):
    # Set에 저장
    phone_set = set(phone_book)
    for phone_number in phone_book:
        # 접두어가 될 수 있는 글자의 길이를 늘려가며(i) 검사
        # ex) :i 까지라서 119는 11까지만 됨
        for i in range(1, len(phone_number)):
            if phone_number[:i] in phone_set:
                return False
    return True
