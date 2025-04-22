def solution(numbers):
    nums = list(map(str, numbers))
    #    최대 4자리(입력 상한이 1000이므로)까지만 봐도 충분
    #    각 문자열을 3~4번 반복
    #    예: "3"  → "3333",   "30" → "3030",   "34" → "3434"
    nums.sort(key=lambda x: x*4, reverse=True)

    # 예외 처리
    if nums[0] == '0':
        return '0'
    
    return "".join(nums)
