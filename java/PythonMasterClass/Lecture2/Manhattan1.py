import sys
input = sys.stdin.readline

input_list = list(map(int, input().rstrip().split()))

mx = max(input_list)
mn = min(input_list)

A = abs(mx-mn)

input_list.remove(mx)
input_list.remove(mn)

B = abs(input_list[0] - input_list[1])

print(A+B)
