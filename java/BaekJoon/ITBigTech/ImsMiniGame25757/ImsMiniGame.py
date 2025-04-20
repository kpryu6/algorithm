def main():
    N, games = input().split(" ")
    N = int(N)
    # s = set()
    # for _ in range(N):
    #   s.add(input())
    s = {input() for _ in range(N)}

    if games == 'Y':
        print(len(s))

    if games == "F":
        print(len(s)//2)

    if games == "O":
        print(len(s)//3)


if __name__ == "__main__":
    main()