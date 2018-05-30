def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''

    list1 = []  # Your code here
    for i in range(max(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            list1.append(i)
        else:
            continue
    return max(list1)


#list1 = []
print(gcdIter(27, 72))
