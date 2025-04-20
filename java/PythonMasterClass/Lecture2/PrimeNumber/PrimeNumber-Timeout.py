# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 소수 : '1'과 '자기 자신' 외의 약수를 가지지 않는 1보다 큰 자연수
import sys
input = sys.stdin.readline

# 2부터 자기 자신 전까지 나눠서 나머지가 0이 아니면 소수 인걸로 했음
def is_prime(a):
	prime = True
	for i in range(2,a):
		if a % i == 0:
			prime = False
	return prime
	
N = int(input())
prime_list = list(map(int, input().rstrip().split()))

ans = 0
for i in range(N):
	if i == 0:
		continue
	# i가 소수이면
	elif is_prime(i+1):
		print(prime_list[i])
		ans += prime_list[i]

print(ans)
	


