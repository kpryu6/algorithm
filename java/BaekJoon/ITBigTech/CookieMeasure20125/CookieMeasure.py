def main():
    N = int(input())

    rows = [input().strip() for _ in range(N)]

    head = []

    # head 찾기
    # 이거 N말고 2로 했더니 런타임에러(IndexError) 났음
    for i in range(N):
        if "*" in rows[i]:
            head.append(i+2)
            head.append(rows[i].index("*")+1)
            break

    left_hand = 0
    right_hand = 0
    waist = 0
    left_leg = 0
    right_leg = 0

    for i in range(head[0]-1, N):
        # 팔 길이
        if i == head[0]-1:
            for j in range(head[1]-1):
                if rows[i][j] == "*":
                    left_hand += 1
            for j in range(head[1], len(rows[0])):
                if rows[i][j] == "*":
                    right_hand += 1
        # 허리 길이
        elif rows[i][head[1]-1] == "*":
            waist += 1
        # 다리 길이
        else:
            if head[1] > 1 and rows[i][head[1] - 2] == "*":
                left_leg += 1
            if head[1] < len(rows[0]) and rows[i][head[1]] == "*":
                right_leg += 1
        


    print(head[0],head[1])
    print(left_hand, right_hand, waist, left_leg, right_leg)

if __name__ == "__main__":
    main()
                
        

        