N, new, P = map(int, input().split())

if N > 0:
    rank_list = list(map(int, input().split()))
else:
    rank_list = []

rank = 1

# 리스트로 들어가봅시다
for i in range(N):
    if new > rank_list[i]:
        break
    elif new == rank_list[i]:
        break
    else:
        rank += 1

# 꽉 차있을 때 마지막과 같을 경우 못넣음
if N == P and N > 0 and new <= rank_list[-1]:
    print(-1)
else:
    print(rank)
