def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    counter = 0
    x= True
    while x == True:
        user2 = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if user2 == 'r':
            counter += 1
            if counter >= 2:
               playHand(dealHand(HAND_SIZE), wordList, HAND_SIZE)
            elif counter <= 1:
                print("You have not played a hand yet. Please play a new hand first!")
        elif user2 == 'e':
            x = False
            break
        # try: 
            #playHand(dealHand(HAND_SIZE), wordList, HAND_SIZE)
        # except nameerror:
            #print("You have not played a hand....")
        elif user2 == 'n':
            counter += 1
            playHand(dealHand(HAND_SIZE), wordList, HAND_SIZE)
            playGame(wordList)
            x = False
            
        else:
            print("The input was invalid")
#Does not replay the same hand.