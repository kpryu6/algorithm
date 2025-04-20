def main():
    # 사용자 입력
    user_input = input()
    # 입력 리스트
    params = user_input.split()

    if len(params) != 4:
        print("파라미터를 4개 입력하세요.")
        return

    try:
        # 각 파라미터 정수로 변환 후 조건 확인
        pv = [int(param) for param in params]
        if all(0 < value <= 50000 for value in pv):
            H, W, N, M = pv

            # 가로에 채울 수 있는 경우 
            check_rows = ((H-1) // (N + 1)) + 1
            check_cols = ((W-1) // (M + 1)) + 1
            
            # 배열 출력
            # for row in array:
            #     print(row)

            answer = check_rows * check_cols
            print(answer)
        else:
            print("각 파라미터는 0 초과 50000 이하여야 함")
    except ValueError:
        print("모든 파라미터는 정수여야 함")


    
# 메인함수 호출
if __name__ == "__main__":
    main()
