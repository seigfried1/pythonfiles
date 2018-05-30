from sys import exit
s = 's'
alphabeta = "abcdefghijklmnopqrstuvwxyz"


def isIn(char, aStr):
    i = 12

    stringing = True
    while stringing:
        guess = alphabeta[i]
        print(guess)
        userin = input("If guess is higher type 'h', lower type 'l', and correct type 'c': ")
        if userin == 'h':
            i = i//2
            guess = alphabeta[i]
        elif userin == 'l':
            i = 12 + (i//2)
            guess = alphabeta[i]
        elif userin == 'c':
            print("The guess is: {}".format(guess))
            stringing = False
            exit(0)

        else:
            print("No char other than alphabets allowed!")


print(isIn(s, alphabeta))
