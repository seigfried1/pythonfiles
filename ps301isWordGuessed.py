def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    i = 0
    ls = []
    while i < len(secretWord):
        if secretWord[i] in lettersGuessed:
            ls.append(True)
        else:
            ls.append(False)
        i += 1
    #print(ls)
    if False in ls:
        return False
    else:
        return True
