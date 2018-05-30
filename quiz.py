qa = [["Number of continents", 7], ["Name of our galaxy", "Milky Way"], ["The tambourine man with a Nobel", "Bob Dylan"]]


def main():
	print("Welcome to the Quiz")
	inputs = question(qa)
	factcheck(inputs)
	# question(qa)

def question(ls):
	i = 0
	inputs = []
	while i < len(qa):
		user = input(ls[i][0] )
		inputs.append(user)
		i += 1
	# print(inputs)
	return inputs

def factcheck(inputs):
	j = 0
	while j < len(inputs):
		if str(qa[j][1]) == inputs[j]:
			print(qa[j][0], "is", qa[j][1])
			j += 1
		elif str(qa[j][1]) != inputs[j]:
			print(qa[j][0], "is not", qa[j][1])
			j += 1
		
if __name__ == '__main__':
    main()


