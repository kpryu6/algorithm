'''
각 숫자가 0과 1의 출력 개수를 저장하는 배열을 만들어보자
DP0 = []
DP1 = []

'''
T = int(input())

DP0 = [0] * 41
DP1 = [0] * 41


for _ in range(T):
    N = int(input())
    for i in range(N+1):
        if i == 0:
            DP0[i] = 1
        elif i == 1:
            DP1[i] = 1
        else:
            DP0[i] = DP0[i-1] + DP0[i-2]
            DP1[i] = DP1[i-1] + DP1[i-2]

    print(DP0[N], DP1[N])

