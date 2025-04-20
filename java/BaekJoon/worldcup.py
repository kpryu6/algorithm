import sys
input = sys.stdin.readline

win = 0
draw = 0
lose = 0
cnt = 0
for i in range(4):
    result = list(input().rstrip().split())
    
    for j in range(0,len(result),3):
        win += int(result[j])
    
    for j in range(1,len(result),3):
        if j != 0:
            cnt += 1 
        draw += int(result[j])
    
    for j in range(2,len(result),3):
        lose += int(result[j])
    print(cnt // 2)
    if win == lose and cnt // 2 == 0:
        print(1, end="")
    else:
        print(0, end="")

