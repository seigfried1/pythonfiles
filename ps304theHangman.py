def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''  
       # dsfds
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    n = 8
    print('-----------')

    guessed = ''
    guessedlis = []
    replist = []
    newlis = []
    while n >= 1:
        print("You have {} guesses left".format(n))
        print("Available Letters:", getAvailableLetters((list(guessed))))
        guess = input("Please guess a letter: ")
        guess_low = guess.lower()
        guessed += guess_low
        # print(guessed)
        guessedlis.append(guessed)
        # print(replist)
        if isWordGuessed(secretWord, guessed):
            print("Good guess: {}".format(getGuessedWord(secretWord, guessed)))
            print("-----------")
            print("Congratulations, you won!")
            n = 0
        elif guess in replist:
            print("Oops! You've already guessed that letter: {}".format(
                getGuessedWord(secretWord, guessed)))
            print("-----------")
            n += 1
        elif guess in secretWord:
            print("Good Guess: {}".format(getGuessedWord(secretWord, guessed)))
        elif guess not in secretWord:
            print("Oops! That letter is not in my word: {}".format(
                getGuessedWord(secretWord, guessed)))
            print("-----------")
            replist.append(guessed[-1])
        replist.append(guessed[-1])
        n -= 1
    if not isWordGuessed(secretWord, guessed):
        print("Sorry, you ran out of guesses. The word was else.")
        # print(replist)

