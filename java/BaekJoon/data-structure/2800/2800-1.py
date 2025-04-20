'''
itertoolsㅇㅔ combination쓰기
'''
from itertools import combinations
import sys
input = sys.stdin.readline

_list = list(input().rstrip())
stk = []
gwalho = []
answers = set()

# '('와 ')'의 인덱스
for i in range(len(_list)):
    if _list[i] == '(':
        stk.append(i)
    elif _list[i] == ')':
        gwalho.append((stk.pop(),i))

for i in range(len(gwalho)):
    for comb in combinations(gwalho, i+1):
        temp = _list[:]
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = ""
            answers.add("".join(temp))

for ans in sorted(answers):
    print(ans)

