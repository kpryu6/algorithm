from itertools import combinations
import sys
input = sys.stdin.readline
# (0/(0))
# ['(', '0', '/', '(', '0', ')', ')']
_list = list(input().rstrip())
stk = []
# 쌍을 이루는 괄호의 index 쌍을 모은 리스트
indices = []
answers = set()

for i in range(len(_list)):
    if _list[i] == '(':
        stk.append(i)
    elif _list[i] == ')':
        indices.append((stk.pop(), i))

# print(indices)

for i in range(len(indices)):
    for comb in combinations(indices, i+1):
        # ((6, 10),)
        # ((3, 11),)
        # ((0, 12),)
        # ((6, 10), (3, 11))
        # ((6, 10), (0, 12))
        # ((3, 11), (0, 12))
        # ((6, 10), (3, 11), (0, 12))
        # print(comb)
        temp = _list[:]
        # print(temp)
        # '('와 ')' 제거 (del이나 remove 시 index에 영향을 주기에 이렇게 함) 
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = ""
        answers.add("".join(temp)) # 중복 제거를 위한 set
        
for item in sorted(list(answers)):
    print(item)

