'''
A -> B 메시지 획득
숫자 N개로 이루어진 수열
모두 <= C
빈도 순 대로 정렬
X Y Y Y 일경우
Y Y Y X 여야 함

X Y Y X 일 경우
X X Y Y
'''
import sys
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
_list = list(map(int, input().rstrip().split()))
freq = [0] * (N+1)
prior_cnt = [10000000000] * (N+1)
# 빈도가 높으면 앞에 있어야 함
# 횟수 같으면 먼저 나온 게 앞에 있어야 함

# 우선순위 및 빈도 저장
prior = 1
for num in _list:
    freq[num] += 1
    if freq[num] == 1:
        prior_cnt[num] = prior
        prior += 1

# 우선순위가 낮은 인덱스부터 빈도수를 -1씩 하며 출력하기
# 이러면 시간복잡도 미치게 올라감 
first_idx = prior_cnt.index(min(prior_cnt))
print(first_idx)


print(freq)
print(prior_cnt)
