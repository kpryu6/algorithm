# 종류별 1가지 의상
# 메이플 코디임
# 최소 1개의 이상은 입음

# 서로다른 옷의 조합 수 return


# 종류 : 이름들?
# 전체 개수 + 각 개수 곱하기

# 예: {"headgear": ["yellow_hat", "green_turban"], "eyewear": ["blue_sunglasses]}
# 2+1 + 2*1 = 5

'''
**위에 처럼 하면 안됨**

1. 각 종류에 따라 안입는 경우도 포함(+1)
2. 전체 경우의 수에서 모두 안입는 경우 제거(-1)

(종류1_의상수 + 1) × (종류2_의상수 + 1) × ... × (종류n_의상수 + 1) - 1

'''

from collections import Counter

def solution(clothes):
    answer = 1
    cnt = Counter()
    for cloth in clothes:
        cnt[cloth[1]] += 1
    cnt_list = list(cnt.values())
    
    for i in range(len(cnt_list)):
        answer *= (cnt_list[i]+1)
    
        
    return answer -1
