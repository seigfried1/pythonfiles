def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    totalus = 0
    counter  = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) >= 1:
        # Display the hand
        #print("Current Hand: {}".format(print(displayHand(hand))))
        
        print("Current Hand: ", end=""), displayHand(hand)
        # Ask user for input
        user = input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if user == '.':
            # End the game (break out of the loop)
            break
        elif user != '.':       
        # Otherwise (the input is not a single period):
            if not isValidWord(user, hand, wordList):
            # If the word is not valid:
                print("Invalid word, please try again.")
                counter = counter
                # Reject invalid word (print a message followed by a blank line)
            elif isValidWord(user, hand, wordList):
            # Otherwise (the word is valid):
                if counter > 0 and calculateHandlen(hand) == len(user):
                    totalus += getWordScore(user, calculateHandlen(hand))
                    totalus -= 50
                    print('" {0} " has earned {1} points. Total score: {2} points'.format(user, getWordScore(user, calculateHandlen(hand)) - 50, totalus))
                else:    
                    totalus += getWordScore(user, calculateHandlen(hand))
                    print('" {0} " has earned {1} points. Total score: {2} points'.format(user, getWordScore(user, calculateHandlen(hand)), totalus))
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                hand = updateHand(hand, user)
                # Update the hand 
                counter += 1
    if user == ".":
        print("Goodbye! Total score: {}".format(totalus))
    else:
        print("Run out of letters. Total score: {} points".format(totalus))