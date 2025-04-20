import sys

def main():
    m = int(sys.stdin.readline().strip())
    s = set()

    for _ in range(m):
        # strip : 문자열 선행, 후행 공백 모두 제거
        cmd = sys.stdin.readline().strip()
        if ' ' in cmd:
            op, num = cmd.split()
            num = int(num)
        else:
            op = cmd
        
        if op == "add":
            s.add(num)
        elif op == "check":
            if num in s:
                print(1)
            else:
                print(0)
        elif op == "remove":
            s.discard(num)
        elif op == "toggle":
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        elif op == "all":
            s = set(range(1,21))
        elif op == "empty":
            s.clear()
        

if __name__ == "__main__":
    main()