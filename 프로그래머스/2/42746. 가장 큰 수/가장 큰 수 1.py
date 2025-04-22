from functools import cmp_to_key

def solution(numbers):
    # 숫자들을 문자열로 바꿔서 비교
    numbers = list(map(str, numbers))
    
    # 커스텀 비교 함수
    def compare(x, y):
        if x + y > y + x:
            return -1  # x가 앞에 와야 함
        elif x + y < y + x:
            return 1   # y가 앞에 와야 함
        else:
            return 0   # 같음
    
    # 정렬
    numbers.sort(key=cmp_to_key(compare))
    
    # 모두 0일 경우 예외 처리
    if numbers[0] == '0':
        return '0'
    
    # 이어붙여서 결과 반환
    return ''.join(numbers)
