def main():
    k = int(input())
    # 등차수열

    n = 1
    while True:
        if k == 1:
            break
        if 3 * n * n + 3 * n + 1 >= k:
            n += 1
            break
        n += 1
    
    print(n)


if __name__ == "__main__":
    main()