N = int(input())

people = [list(map(int, input().split())) for _ in range(N)]

# 순위 리스트
ranks = [1] * N

for i in range(N):
    rank = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            ranks[i] += 1

print(" ".join(map(str, ranks)))
    

            
