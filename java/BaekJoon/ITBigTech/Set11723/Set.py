# Memory 최적화 버전 -> 입력과 출력 모두 저장X

import sys

def main():
    
    m = int(sys.stdin.readline().strip())
    s = set()

    for _ in range(m):
        # 명령어 읽고 바로 처리
        command = sys.stdin.readline().strip()

        if ' ' in command:
            op, num_str = command.split()
            num = int(num_str)
        else:
            op = command

        if op == "add":
            s.add(num)
        elif op == "remove":
            s.discard(num)
        elif op == "check":
            print('1' if num in s else '0')
        elif op == "toggle":
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        elif op == "all":
            s = set(range(1, 21))
        elif op == "empty":
            s.clear()

if __name__ == "__main__":
   main()
