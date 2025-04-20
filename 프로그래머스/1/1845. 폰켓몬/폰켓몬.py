'''
종류 최대한 많이 선택해야 함
'''
def solution(nums):
    return min(len(set(nums)), len(nums)/2)