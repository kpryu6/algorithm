'''
괄호 제거 해서 나오는 모든 식 출력
1. 괄호의 인덱스 -> 괄호의 쌍 찾기
2. 괄호 쌍의 조합을 이용한 식 만들기
3. 식 출력
'''
import sys
from itertools import combinations
input = sys.stdin.readline

stk = []
indices = []
answers = set()

_list = list(input().rstrip())
# FIFO를 이용한 괄호 인덱스 저장
for i in range(len(_list)):
    if _list[i] == '(':
        stk.append(i)
    elif _list[i] == ')':
        indices.append((stk.pop(), i))

for i in range(len(indices)):
    # 1개짜리, 2개짜리, 3개짜리 comb
    for comb in combinations(indices, i+1):
        temp = _list[:]
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = ""
            answers.add("".join(temp))

for ans in sorted(answers):
    print(ans)
