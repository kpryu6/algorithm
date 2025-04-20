'''
N M # 검사 # 문자열 주어지는거

'''
import sys
input = sys.stdin.readline
_list = []
N, M = map(int, input().rstrip().split())
for _ in range(N):
    _list.append(input().rstrip())

cnt = 0
# 이중 for문을 어떻게 없을까...
for _ in range(M):
    _input = input().rstrip()
    if _input in _list:
            cnt += 1
print(cnt)
