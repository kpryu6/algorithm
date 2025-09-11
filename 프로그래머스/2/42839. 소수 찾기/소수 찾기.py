'''
numbers로 만들 수 있는 소수 개수
소수 = 약수가 1과 자기자신
2 3 5 7 11 13 17 19 23

만들 수 있는 숫자 (17)
1. 1개 뽑아서 -> 1, 7
2. 2개 뽑아서 -> 17, 71

만들 수 있는 숫자 (011)
1. 1개뽑아서 -> 0, 1
2. 2개 뽑아서 -> 10, 11
3. 3개 뽑아서 -> 101, 110, 011(11)
'''
from itertools import permutations

# 소수 판별 함수
def isPrime(num):
    # 1이면 그냥 아웃
    if num < 2:
        return False
    # 나눠지면 아웃 - 제곱근까지만 해도 됨 - 효율 up
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    
# numbers로 만들 수 있는 숫자 모두 만들어서 isPrime으로 +
def solution(numbers):
    answer = 0
    li = list(numbers)
    # 어떻게 만들 수 있는 숫자를 다 찾아내냐?
    # 순열(Permutations)
    # 서로 다른 n개에서 r개를 선택하여 순서대로 나열하는 경우의 수
    # 중복 제거
    all_numbers = set()
    
    for i in range(1, len(li)+1):
        perms = permutations(li, i)
        for p in perms:
            num = int(''.join(p))
            all_numbers.add(num)
    
    for n in all_numbers:
        if isPrime(n):
            answer += 1
            
    return answer