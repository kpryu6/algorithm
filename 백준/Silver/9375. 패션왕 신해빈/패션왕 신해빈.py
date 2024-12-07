'''
조합!

'''
import sys
from collections import defaultdict
input = sys.stdin.readline
T = int(input().rstrip())



for _ in range(T):
    n = int(input().rstrip())
    C = defaultdict(list)
    visited = defaultdict(int)

    for _ in range(n):
        name, kind = input().rstrip().split()
        C[kind].append(name)

    result = 1
    for kind in C:
        result *= (len(C[kind]) + 1)
    
    print(result-1)
            