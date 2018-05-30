def max_val(t):
    lis = []
    if type(t) is tuple:
        t = tutolis(t)
        for i in range(len(t)):
            if type(t[i]) is tuple:
                t[i] = tutolis(t[i])
                # print(t[i])
                for k in range(len(t[i])):
                    lis.append(t[i][k])
            elif type(t[i]) is list:
                tlist = t[i]
                for j in range(len(tlist)):
                    if type(t[i][j]) is int:
                        lis.append(t[i][j])
                    elif type(t[i][j]) is list:
                        ttlist = t[i][j]
                        for m in range(len(ttlist)):
                            lis.append(ttlist[m])
            elif type(t[i]) is int or float:
                lis.append(t[i])
    return max(lis)


def tutolis(x):
    x = list(x)
    return x


t = (5, (1, 2), [[1], [2]])
print(max_val(t))
# list_t = list(t)
# print(list_t)
# low = []
# for i in range(len(list_t)):
#     print(list_t[i])
#
#
