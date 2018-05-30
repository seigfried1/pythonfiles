def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    d2 = {}
    lisa = []
    # keylist = list(d.keys())
    # valuelist = list(d.values())
    # counter = 0
    # while counter <= len(keylist)-1:
    #     d2[valuelist[counter]] = [keylist[counter]]
    #     counter += 1
    # return d2

    for i, j in d.items():
        # ij = list(i)
        lisa.append((j, i))
    #print(lisa)
    lk = []
    lkb = []
    for i in range(len(lisa)):
        ak = (lisa[i])
        #print(ak[0])
        if ak[0] not in lk:
            lk.append(ak[0])
            lkb.append(ak[1])
            d2[ak[0]] = [ak[1]]
        elif ak[0] in lk:
            d2[ak[0]] = [lkb[-1], (ak[1])]
    return d2


d = {1: 10, 2: 20, 3: 30, 4: 30}
print(dict_invert(d))
