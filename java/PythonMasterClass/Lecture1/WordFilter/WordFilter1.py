# 내가 끄적인 것 (틀림)
# 문자열 인덱스 가지고 check가 S_len까지 되면 그 이전꺼 삭제할 예정이였으나 실패
S_len, E_len = map(int, input().split())
S = input()
E = input()
answer = []
check = 0

for i in range(E_len):
	answer.append(E[i])

if S in E:
	for i in range(E_len):
		if S[i%S_len] == E[i]:
			check += 1
			if check == S_len:
				for j in range(i, -1, i-check):
					answer.pop()

print(''.join(answer))
