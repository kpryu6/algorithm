import sys
input = sys.stdin.readline

dict = {}

N, M = map(int, input().rstrip().split())
for i in range(N):
    pokemon = input().rstrip()
    dict[i+1] = pokemon
    dict[pokemon] = i+1

for _ in range(M):
    quiz = input().rstrip()
    if quiz.isdigit():
        print(dict[int(quiz)])
    else:
        print(dict[quiz])