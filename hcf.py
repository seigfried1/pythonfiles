listed = []
listed2 = []


def factorialnum_list(x):
    for i in range(1, x + 1):
        if x % i == 0:
            listed.append(i)
            # print(listed)
            # print(i)

    return listed


def factorialnum_list2(y):
    for i in range(1, y + 1):
        if y % i == 0:
            listed2.append(i)
            # print(listed)
            # print(i)

    return listed2


def hcf(a, b):
    factorialnum_list(a)
    factorialnum_list2(b)
    return (max(list(set(listed).intersection(listed2))))

    # print(alist)
    # print(blist)


# print(factorialnum(27)
print(hcf(26, 20))
# print(max(factorialnum_list(b)))
