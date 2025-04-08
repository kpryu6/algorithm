# N/2 가져가~
# 번호 -> 종류

# 다양한 종류 가지고싶음

# nums = 폰켓몬 종류 번호 담긴 배열
# 최대로 선택할 수 있는 종류 개수 출력

# for문 N/2로

[1,2,3,4,5,6]


def solution(nums):
    N = len(nums)
    answer = set()
    for i in range(N):
        answer.add(hash(nums[i]))
    if len(answer) > N//2:
        return N//2
    else:
        return len(answer)
        
        
        
    