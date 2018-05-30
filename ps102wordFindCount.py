s = '' #any given word, example 'azcbobobegghakl'
count = 0
for i in range(len(s) + 1):
    if s[i:i+3] == 'bob':
        count += 1
    else:
        count = count
print("Number of times bob occurs is: {}".format(count))
