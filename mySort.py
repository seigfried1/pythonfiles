nu = [2, 3, 45, 5, 23, 4, 12, 6, 33, 46, 33]
anyd = 0
list2 = []
while len(nu) > 0:
    for i in nu:
        if i > anyd:  # searches for a number that is greater than 0
            anyd = i  # assigns that number to i
    list2.append(anyd) #appends the maximum number
    nu.remove(anyd)  # removes that number from the original list
   # print(list2)
    anyd = 0
print(list2[::-1])
