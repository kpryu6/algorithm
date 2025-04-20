def main():

    inputs = []

    while True:
        # 공백 제거
        user_input = input().strip()
        if user_input == "0 0 0":
            break

        params = user_input.split()
        if len(params) != 3:
            print("파라미터 3개 입력하세요")
            continue
        
        try:
            values = [int(param) for param in params]
            if all(0 < value <= 1000 for value in values):
                inputs.append(values)

            else:
                print("0 초과 1000 이하여야 함")
        except ValueError:
            print("모든 파라미터는 정수여야 함")
            continue

    for data in inputs:
        a, b, c = data
        # 삼각형 유효성 검사
        if a + b > c and a + c > b and b + c > a:
            # 세 변 모두 같을 때
            if a == b == c:
                print("Equilateral")
            # 두 변만 같을 때
            elif a == b or b == c or a == c:
                print("Isosceles")
            else:
                print("Scalene")
        else:
            print("Invalid")

if __name__ == "__main__":
    main()