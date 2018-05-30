s = '' # any given word.
vowels = 'aeiou'
count = 0
for i in range(len(s)):
    if s[i] in vowels:
        count += 1
    else:
        count = count
print('Number of vowels: {}'.format(count))