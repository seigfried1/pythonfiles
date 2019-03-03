def find_root(x):
	count = 0
	while count <= x:
		if count * count == x:
			return "Root of " + str(x) + " is " + str(count)
		count += 1
	return str(x) + " has no root"

# print(find_root(25))

def find_upto_fifth_pwr(x):
	count = 0
	while count <= x:
		for i in range(6):
			if count ** i == x:
				return count, i
		count += 1
	return "nope"

# print(find_upto_fifth_pwr(4))