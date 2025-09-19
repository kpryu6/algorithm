'''
Numbers로 target 만들기
dfs()로 파야됨
'''
def solution(numbers, target):
    answer = 0
    def dfs(index,current_sum):
        
        if index == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0
        
        case_plus = dfs(index+1, current_sum + numbers[index])
        case_minus = dfs(index+1, current_sum - numbers[index])
        
        return case_plus + case_minus
    answer = dfs(0,0)
    return answer