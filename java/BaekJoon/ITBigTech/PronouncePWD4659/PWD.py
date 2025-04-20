def main():

    list = ['a', 'e', 'i', 'o', 'u']

    while True:
        pwd = input().strip()
        if pwd == "end":
            break
        
        # 모음 포함 유무
        cnt = 0
        for i in list:
            if i in pwd:
                cnt += 1
        if cnt < 1:
            print(f'<{pwd}> is not acceptable.')
            continue

        # 모음 연속 3개 or 자음 연속 3개
        three = False
        for i in range(len(pwd)-2):
            if pwd[i] in list and pwd[i+1] in list and pwd[i+2] in list:
                three = True
            elif pwd[i] not in list and pwd[i+1] not in list and pwd[i+2] not in list:
                three = True
        if three:
            print(f'<{pwd}> is not acceptable.')
            continue

        # 같은 글자 연속 2개이지만 ee나 oo면 continue
        double = False
        for i in range(len(pwd)-1):
            if pwd[i] == pwd[i+1]:
                if pwd[i] == 'e' or pwd[i] == 'o':
                    continue
                else:
                    double = True
        if double:
            print(f'<{pwd}> is not acceptable.')
            continue

        # 적합
        print(f'<{pwd}> is acceptable.')

if __name__ == "__main__":
    main()