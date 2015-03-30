# 6.00 Problem Set 3
#
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def hangman():
    """
    The ultimate game of hangman
    """
    the_word = choose_word(wordlist)
    remaining_guesses = 5
    letters = ""
    correct_letters = ""
    print "The game begins"
    print "I am thinking of a word that is %d letters long." % len(the_word)
    print "\n"
    print "You can guess letters correctly up to 5 times. Good luck!"
    print "\n"
    while remaining_guesses >= 1:
        print "Here's what you know about my word: " + str(renderWord(the_word, letters))
        print "The following letters remain: " + str(unusedLetters(letters))
        print "You have %d guesses remaining." % remaining_guesses
        print "\n"
        user_guess = raw_input("Guess a letter in the word: ")
        if user_guess in the_word:
            if user_guess in letters:
                print "You have already guessed %s!" % user_guess
            else:
                print "Good guess! %s was indeed in the word." % user_guess
                print "\n"
                letters += user_guess
        else:
            if user_guess in letters:
                print "You have already guessed %s!" % user_guess
            else:
                print "Sorry, %s is not in my word." % user_guess
                print "\n"
                letters += user_guess
                remaining_guesses -= 1

        if str(renderWord(the_word, letters)) == the_word:
            victory()
            break

    defeat()


def renderWord(word, letters):
    rendered_word = ""
    for letter in word:
        if letter in letters:
            for i in letters:
                if letter == i:
                    rendered_word += i
        else:
            rendered_word += "_"

    return rendered_word

def unusedLetters(letters):
    unused_letters = string.ascii_lowercase
    for i in unused_letters:
        if i in letters:
            unused_letters =  unused_letters.replace(i, "")
        else:
            pass

    return unused_letters

def victory():
    print "Congratulations, you successfully guessed the word!"

def defeat():
    print "You ran out of guesses - you lose!"

hangman()