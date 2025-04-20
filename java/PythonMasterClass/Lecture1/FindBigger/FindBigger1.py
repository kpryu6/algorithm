# 이것이 진정 도른자인가 생각을 하고 풀자 막무가내로 풀지말고
# eval을 생각했어야지 이렇게 풀면 RuntimeError 납니다.
exp1, exp2 = map(str, input().split())

operations = ["+", "-"]

for op in operations:
	if op in exp1:
		front, behind = map(str, exp1.split(op))
		if "*" in front:
			word1, word2 = map(int, front.split("*"))
			word = word1 * word2
			if op == "+":
				ans1 = word + int(behind)
			else:
				ans1 = word - int(behind)
		elif "*" in behind:
			word1, word2 = map(int, behind.split("*"))
			word = word1 * word2
			if op == "+":
				ans1 = word + int(front)
			else:
				ans1 = word - int(front) 
		else:
			if op == "+":
				ans1 = int(front) + int(behind)
			else:
				ans1 = int(front) - int(behind)
	
	if op in exp2:
		front, behind = map(str, exp2.split(op))
		if "*" in front:
			word1, word2 = map(int, front.split("*"))
			word = word1 * word2
			if op == "+":
				ans2 = word + int(behind)
			else:
				ans2 = word - int(behind)
		elif "*" in behind:
			word1, word2 = map(int, behind.split("*"))
			word = word1 * word2
			if op == "+":
				ans2 = word + int(front)
			else:
				ans2 = word - int(front)
		else:
			if op == "+":
				ans2 = int(front) + int(behind)
			else:
				ans2 = int(front) - int(behind)
				
print(max(ans1, ans2))
