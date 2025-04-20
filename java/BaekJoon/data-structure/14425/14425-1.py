N, M = map(int,input().split())
_list = []
for _ in range(N):
    _list.append(input())

cnt = 0
for _ in range(M):
    word = input()
    if word in _list:
        cnt += 1

print(cnt)
