user_input = input()
splits = user_input.split()

if len(splits) != 4:
    print("파라미터가 4개여야 함")

values = [int(split) for split in splits]
if all(0 < value <= 50000 for value in values):
    H, W, N, M = values
    
    check_rows = ((H - 1) // (N + 1)) + 1
    check_cols = ((W - 1) // (M + 1)) + 1

    answer = check_rows * check_cols
    print(answer)
else:
    print("0 초과 50000 이하인 파라미터를 입력하세요")



