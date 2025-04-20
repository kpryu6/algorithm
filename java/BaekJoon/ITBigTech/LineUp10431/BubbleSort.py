def Bubblesort(List):
    global steps
    for i in range(len(List)-1 , 0, -1):
        for j in range(i):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
                steps += 1

P = int(input())
for _ in range(P):
    # 첫번째 값 : N, 나머지 값 : x
    N, *x = map(int, input().split())
    steps = 0
    Bubblesort(x)
    print(N, steps)

