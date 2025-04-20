N = int(input())
S = input()
answer = []

for s in S:
    if s.isupper():
        answer.append(s.lower())
    elif s.islower():
        answer.append(s.upper())
print(''.join(answer))
