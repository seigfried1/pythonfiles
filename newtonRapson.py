num = 25
count = 0
guess = num/2
epsilon = 0.01

while abs(guess**2 - num) > epsilon:
	count += 1
	print(guess)
	# Newton-Raphson's method for better approximation
	guess = guess - (((guess**2)-num)/(2*guess))
print(guess)
print(count)