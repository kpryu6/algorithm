# Bubble Sort로 안한 거
# 굳이 이렇게까지?
import sys

def count_back_steps(test_case):
    heights = test_case[1:]
    lineup = []
    steps = 0

    for height in heights:
        position = len(lineup)
        for i in range(len(lineup)):
            if lineup[i] > height: 
                position = i
                break
        steps += len(lineup) - position
        lineup.insert(position, height)

    return steps

def main():
    input = sys.stdin.readline
    N = int(input())  

    results = []

    for i in range(1, N + 1):
        test_case = list(map(int, input().split()))
        T = test_case[0]
        steps = count_back_steps(test_case)
        results.append(f"{T} {steps}")
    
    for result in results:
        print(result)
    

if __name__ == "__main__":
    main()