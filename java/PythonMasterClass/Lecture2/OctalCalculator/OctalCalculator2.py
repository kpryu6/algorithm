import sys
input = sys.stdin.readline

N = int(input())
S = sum(list(map(int, input().split())))
#
print(oct(S)[2:])
