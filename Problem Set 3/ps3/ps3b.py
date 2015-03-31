from ps3a import *
import time
from perm import *
import random

HAND_SIZE = random.randint(3, 8)
#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    possible_words = []
    # For large HAND_SIZE values the computer will take some time to sort through the permutations
    print "Computer is thinking..."
    for wordlen in range(1, HAND_SIZE + 1):
        # Get all possible words
        perms = get_perms(hand, wordlen)
        # Filter possible words
        for word in perms:
            if word in word_list:
                possible_words.append(word)

    # Debugging note
    # print "Computer has contemplated all possible words. Making calculations..."

    score = 0
    comp_word = None

    for word in possible_words:
        word_score = get_word_score(word, HAND_SIZE)
        if word_score > score:
            score = word_score
            comp_word = word
        else:
            comp_word = None

    # Debugging note
    # print "Computer has arrived at a conclusion."

    if comp_word != None:
        return comp_word
    else:
        return None

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed,
       the remaining letters in the hand are displayed, and the computer
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...
    hand_played = False
    hand_total = 0
    display_hand(hand)

    while hand_played != True:
        user_word = comp_choose_word(hand, word_list)

        if len(hand) == 0 or user_word == None:
            hand_played == True
            break

        if user_word in word_list:
            word_score = get_word_score(user_word, len(hand))
            hand_total += word_score
            print "Computer played %s for a total of %d points" % (user_word, word_score)
            update_hand(hand, user_word)
            display_hand(hand)

        else:
            print "Invalid word, please try again."

    print "Round over."
    print "Computer made a total of %d points this round." % hand_total

#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    print "Welcome to pseudo-Scrabble!"
    print "To play a hand, enter 'n'"
    print "To play the last hand again, enter 'r'"
    print "To exit, enter 'e'"

    last_hand = deal_hand(HAND_SIZE)

    game_on = True

    while game_on == True:
        user_input = raw_input("> Enter a command: ")
        # Exit the game
        if user_input == 'e':
            game_on == False
            break
        # Start a new hand
        elif user_input == 'n':
            user_comp = raw_input("Enter 'u' to play this round yourself; enter 'c' to have the computer play.")
            # The user plays the game
            if user_comp == 'u':
                last_hand = deal_hand(HAND_SIZE)
                play_hand(last_hand.copy(), word_list)
            # The computer plays the game
            elif user_comp == 'c':
                last_hand = deal_hand(HAND_SIZE)
                comp_play_hand(last_hand.copy(), word_list)
            else:
                print "Invalid command, please enter a valid command"
        # Repeat the last hand
        elif user_input == 'r':
            user_comp = raw_input("Enter 'u' to play this round yourself; enter 'c' to have the computer play.")
            if user_comp == 'u':
                play_hand(last_hand.copy(), word_list)
            elif user_comp == 'c':
                comp_play_hand(last_hand.copy(), word_list)
            else:
                print "Invalid command, please enter a valid command"

        else:
            print "Invalid command, plese enter a valid command"

    exit()

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)


