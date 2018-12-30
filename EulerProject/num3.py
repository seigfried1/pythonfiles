#Project Euler #3:
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
def factor(num):
	factors = []
	for i in range(2,num):
		if num%i == 0:
			num = num/i
			factors.append(i)
	return factors

def find_prime(num):
	for i in range(2,100):
		if num%i == 0 and num != i:
			return False
	return True

def find_largest_factor_prime(num):
	factor_list = factor(num)
	factor_list_rev = factor_list[::-1]
	for i in factor_list_rev:
		a = find_prime(i)
		if a == True:
			return i
# if __name__ == '__main__':
# 	print(find_largest_factor_prime(13195055))