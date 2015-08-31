'''
Find all prime numbers from 0 to N
----------------------------------
'''

'''
Quadratic O(N^2)
---
'''
#checks if num is prime or not
def is_prime(num):
	for i in range(2, num):
		if num % i == 0: return True
	return False

all_prime_to_N(n):
	for integer in N:
		if is_prime(integer): print integer
	return None

'''
O(N * SQRT(N))
---
'''
#checks if num is prime or not
def is_prime(num):
	for i in range(2, SQRT(num)):
		if num % i == 0: return True
	return False

all_prime_to_N(n):
	for integer in N:
		if is_prime(integer): print integer
	return None
