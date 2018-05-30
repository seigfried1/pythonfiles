s = [2, 3, 45, 5, 23, 4, 12, 6, 33, 46]
things = True
while things:
    def loop(s):
        i = 0
        while i < len(s) - 1:
            if s[i] > s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]
                # print(s)
            else:
                s[i], s[i+1] = s[i], s[i+1]
            i += 1
    for j in range(len(s)-1):
        if s[j] > s[j + 1]:
            loop(s)
        else:
            things = False #probably goes into an infinite loop.

print(s)
