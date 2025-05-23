'''
8 -> 4 => 2 -> 1
8 -> 7 => 6 -> 2 -> 1
10 -> 5 -> 4 -> 2 -> 1
10 -> 9 -> 3 -> 1

1부터 X까지 만들어간다고 생각할 때
각 숫자에서의 최소 연산 횟수를 저장해놓기 (DP의 핵심)
(bottom up)
'''
X = int(input())

dp = [0] * 1000001

# dp[i] = 숫자 i를 만들기 위한 최소 연산횟수
for i in range(2, X+1):
    # 전꺼랑 비교
    dp[i] = dp[i-1] + 1 # 1 빼주는 경우 
    
    # 2 나눈거와 비교
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    
    # 3 나눈거와 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[X])
