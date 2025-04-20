from collections import defaultdict


def solution(nums, target):

    nH = defaultdict(int)

    for x in nums:
        y = target - x
        # nH에 있으면 출력
        if y in nH:
            return sorted([x, y])
        # nH에 없는 건 저장
        nH[x] = 1


print(solution([7, 9, 2, 13, 3, 15, 8, 11], 12))
# print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
# print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
# print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
# print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
# print(solution([7, 5, 12, 20], 15))
