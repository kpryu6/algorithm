'''
종 입력
각 종의 비율

dict? 이중list?
dict 로 idx/N 증가하는 식으로
근데 문자열 세야되니까 defaultdict
'''
from collections import defaultdict
import sys

trees = defaultdict(int)
total_trees = 0

for line in sys.stdin:
    tree = line.rstrip()
    # 공백이면
    if not tree:
        break
    trees[tree] += 1
    total_trees += 1

    
for tree, cnt in sorted(trees.items()):
    per = cnt/total_trees * 100
    print(f"{tree} {per:.4f}")


