def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    ls3 = []
    hand2 = hand.copy()
    for i in word:
        if i not in hand2:
            ls3.append(False)
            
        elif hand2[i] <= 0:
            ls3.append(False)

        elif i in hand2:
            hand2[i] -= 1
            ls3.append(True)
            # update the dictionary
       
    #print(hand2)
    if word in wordList and (not False in ls3):
        return True
    elif word in wordList and (False in ls3):
        return False
    elif word not in wordList:
        return False   
