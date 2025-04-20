# 시간복잡도 O^2
def solution(nums, target):
    answer = []
    numlen = len(nums)
    nums = nums.sort()

    for i in range(numlen):
        for j in range(numlen - 1, ):
            if nums[i] + nums[j] == target:
                answer.append(nums[i])
                answer.append(nums[j])
                answer.sort()

    return answer


print(solution([7, 9, 2, 13, 3, 15, 8, 11], 12))
# print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
# print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
# print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
# print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
# print(solution([7, 5, 12, 20], 15))


# n 제한사항 범위가 10000 정도는 n^2으로 해도 된다.
