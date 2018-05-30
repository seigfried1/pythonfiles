def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord_emp = ('_') * len(secretWord)
    s_emplist = list(secretWord_emp)
    i = 0

    while i < len(lettersGuessed):
        j = 0
        while j < (len(secretWord)):
            if lettersGuessed[i] in secretWord[j]:
                num = secretWord.find(lettersGuessed[i])
                s_emplist[j] = lettersGuessed[i]
            j += 1
        # print(s_emplist)
        i += 1
    real_str = "".join(s_emplist)
    return real_str