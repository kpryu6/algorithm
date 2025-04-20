# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 소수 : '1'과 '자기 자신' 외의 약수를 가지지 않는 1보다 큰 자연수
import sys
input = sys.stdin.readline

N = int(input())
prime_list = [0] + list(map(int, input().rstrip().split()))

def Sieve(N):
	# 모두 소수라고 가정
	is_prime = [1 for _ in range(N+1)]
	prime = []
	for i in range(2, N+1):
		# 쳐낸 수들은 continue
		if is_prime[i] != 1:
			continue
		prime.append(i)
		# 배수 쳐내기
		for j in range(2*i, N+1, i):
			is_prime[j] = 0
	return prime

ans = 0
for pr in Sieve(N):
	ans += prime_list[pr]
	
print(ans)
