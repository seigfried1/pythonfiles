# Project Euler #4

"""
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def largest_pal_product(num1, num2):
	while num1 > 0:
		for i in range(num1, num1-11, -1):
			for j in range(num2, num2-11, -1):
				ans_int = i*j
				ans_str = str(ans_int)
				if ans_str == ans_str[::-1]:
					return int(ans_str)
		num1 -= 10

# print(largest_pal_product(999,999))