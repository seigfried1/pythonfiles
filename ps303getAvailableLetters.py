def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    aa = string.ascii_lowercase
    aal = list(aa)
    #print(aa.find(lettersGuessed[1]))
    for i in range(len(lettersGuessed)):
        aal.remove(lettersGuessed[i])
    return ''.join(aal)
