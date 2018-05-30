# perfect cube

cube = int(input("Enter a number: "))
for guess in range(abs(cube)+1):
	if guess ** 3 >= abs(cube):
		#print(cube, "is a perfect cube.")
		break
if guess ** 3 != abs(cube):
	print(cube, "is not a perfect cube")
else:
	if cube < 0:
		guess = -guess
	print("Cube root of " + str(cube) + " is " + str(guess))
	
