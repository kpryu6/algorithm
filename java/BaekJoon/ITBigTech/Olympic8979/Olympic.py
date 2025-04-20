def main():
    # K는 국가이름
    N, K = map(int, input().split())

    if N < 1 or N > 1000:
        print("1<=N<=1000의 조건을 맞추세요")
        return
    if K < 1 or K > N:
        print("1<=K<=N의 조건을 맞추세요")
        return
    
    countries = []

    # countries에 싹 다 넣기
    for _ in range(N):
        T, gold, silver, bronze = map(int, input().split())
        countries.append((T, gold, silver, bronze))

    # 정렬
    countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

    # 국가 K 정보 찾기
    for i in range(N):
        if countries[i][0] == K:
            target = countries[i]
            break

    # K의 등수 계산
    for i in range(N):
        if countries[i][1:] == target[1:]:
            print(i+1)
            break


if __name__ == "__main__":
    main()