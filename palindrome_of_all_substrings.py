# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 19:24:21 2018

@author: RAHUL MISHRA
"""

def perm_and_c(N):
    from itertools import permutations 
    if type(N) == int:
        nls = [x for x in range(N) if x != 0]
    elif type(N) == str:
        nls = []
        for i in N:
            nls.append(i)
    ls = []
    all_pls = []
    count = 0
    while count < len(nls):
        for i in range(len(nls)+1):
            if nls[count:i] != []:
                ls.append(nls[count:i])
        count += 1
#    print(ls)
    for i in ls:
        perm = permutations(i) 
        for j in list(perm):
            all_pls.append(list(j))
   
    return all_pls




ls = []
ans = []
def checker(ru):
    count = 0
    if type(ru) == str:
        rus = [x for x in ru]
    else:
        rus = ru
    if len(rus)%2 != 0:
        rus.pop(rus.index(rus[int(len(rus)/2)])) # Removes the middle word.
    ru = ''.join(rus)
    for i in range(int(len(ru)/2)):
        if ru[i] == ru[len(ru) - (i+1)]:
            count += 1
        elif ru[i] != ru[len(ru) - (i+1)]:
            return False
    if count == int(len(ru)/2):
        return True



def find_palindrome(string):
    dic = {}
    a = perm_and_c(string)
    for i in a:
#        a = palindorme(i)
        j = ''.join(i)
        dic[j] = checker(i)
    return dic
