# Project Euler #7
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def find_prime(num):
	for i in range(2,100):
		if num%i == 0 and num != i:
			return False
	return True

def nth_prime_num(n):
	num = 2
	count = 0
	final_list = []
	while count < n:
		value = find_prime(num)
		if value == True:
			final_list.append(num)
			count += 1
		num += 1
	return final_list[-1]

print(nth_prime_num(1001))