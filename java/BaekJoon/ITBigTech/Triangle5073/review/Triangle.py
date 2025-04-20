def main():

    input_list = []

    while True:
        user_input = input().strip()
        if user_input == "0 0 0":
            break

        splits = user_input.split()
        if len(splits) != 3:
            print("파라미터는 3개여야 합니다")
            continue

        values = [int(split) for split in splits]

        if all(0 < value <= 1000 for value in values):
            input_list.append(values)
        else:
            print("각 파라미터는 0 초과 1000 이하여야 합니다.")

    for data in input_list:
        a, b, c = data
        # 삼각형 유효성 검사부터
        if a + b > c and a + c > b and b + c > a:
            # 변의 길이가 같은 것이 있는가?
            if a == b or b == c or a == c:
                # 세 변 모두 같은가?
                if a == b and b == c:
                    print("Equilateral")
                # 두 변의 길이가 같은가?
                else:
                    print("Isosceles")
            # 변의 길이가 모두 다른가?
            else:
                print("Scalene")
        # 삼각형이 아닌가?
        else:
            print("Invalid")

            

if __name__ == "__main__":
    main()
        
    
