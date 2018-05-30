high, low = 100, 0
print("Please think of a number between 0 and 100! ")
#guess = (high + low)/2
guessing = True
while guessing:
    guess = (high + low)//2
    print("Is your secret number {}".format(guess))
    response = input(
        "Enter 'h' to indicate the guess is too high. \n Enter 'l' to indicate the guess is too low. \nEnter 'c' to indicate I guessed correctly. ")
    if response == 'h':
        high = guess
        guess = (low + guess)//2
    elif response == 'l':
        low = guess
        guess = (high + guess)//2
    elif response == 'c':
        print("Game over. Your secret number was:{} ".format(guess))
        #print("The response is correct.")
        guessing = False
    else:
        print('Sorry, the input was not clear')

#print("Game over. Your secret number was:{} ".format(guess))
