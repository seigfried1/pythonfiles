# approx cube root
# cube = int(input("Enter a number: "))
# epsilon = 0.1
# guess = 0.0
# increment = 0.01
# num_guesses = 0

#Bisection Cube Root
cube = int(input("Enter a number: "))
epsilon = 0.01
num_guesses = 0
low =0
high = cube
guess = (high + low) / 2.0
while abs(guess ** 3 - cube) >= epsilon:
	if guess ** 3 < cube:
		low = guess
	else:
		high = guess
		