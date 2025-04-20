def toggle(k):
    if switch[k] == 0:
        switch[k] = 1
    else:
        switch[k] = 0
    return
    
switch_len = int(input())
switch = list(map(int, input().split()))
people_len = int(input())

for _ in range(people_len):
    gender, num = map(int, input().split())
    # male
    if gender == 1:
        for i in range(0, switch_len):
            if (i+1) % num == 0:
                toggle(i)
    # female
    elif gender == 2:
        num -= 1
        toggle(num)
        left = num-1
        right = num+1
        # 대칭 검사
        while left >= 0 and right < switch_len and switch[left] == switch[right]:
            toggle(left)
            toggle(right)
            left -=1
            right +=1

# print
if switch_len > 20:
    for i in range (0,switch_len,20):
        print(" ".join(map(str, switch[i: i+20]))) 
else:
    print(" ".join(map(str, switch[: switch_len])))
    

