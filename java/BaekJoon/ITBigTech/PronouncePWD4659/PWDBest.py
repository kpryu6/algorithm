import re
while True:
    s = input()
    if s == "end": break
    # s에 aeiou가 있는지 검사
    case1 = len(re.findall('[aeiou]', s)) != 0
    # s에 자음과 모음이 3번연속 있는지 검사
    case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}', s)) == 0
    # ()로 묶은 그룹(e와 o 제외)이 한번 더 반복되는지 검사
    case3 = len(re.findall('([a-df-np-z])\\1', s)) == 0

    if case1 and case2 and case3:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")