# Hash로 풀어보자

def solution(phone_book):
    answer = True
    hash_map = {}
    
    # hash_map의 key들로 phone_number 저장
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    # temp를 따로 만들어서 phone_number과 비교
    for phone_number in phone_book:
        temp = ""
        for num in phone_number:
            temp += num
            # temp가 hash_map에 있으면서 동시에 phone_number가 아니여야 함
            # ex) phone_number = 119, temp = 1195566
            if temp in hash_map and temp != phone_number:
                answer = False
    
    return answer
            
    
