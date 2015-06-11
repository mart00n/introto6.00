# 6.00 Problem Set 3
# Name: Andrew Marton 
# Hangman
# Time: ~130m 


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
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', -1)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # note syntax for split: <stringname>.split() will automatically make list
    print("  ", len(wordlist), "words loaded.")
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

# your code begins here!

# Save me from typing odd syntax...
def listconv(list):
    """
    Returns a string for printing out of a list of strings
    """
    return ''.join(list)

# Function to replace ALL instances of some string in a list
def listreplace(list, string, replacement):
    """
    Returns a list in which all instances of some string replaced with another string
    """
    for i in range(len(list)):
        if list[i] == string:
            list[i] = replacement
    return list

def scoreupdate():
    """
    Updates the score list to contain letters where the _ were
    Checks for instances of the guess in the gameword, accounts for all instances
    """
    for i in range(len(gameword)):
        if gameword[i] == guess:
            score[i] = guess

wordlist = load_words()
gameword = choose_word(wordlist)
wordlen = len(gameword)
print("Welcome to the game, Hangman!")
print("I'm thinking of a word that is", wordlen, "letters long...")
#print(gameword) #debug
parts = 6
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# make list of _ to print for user
score = [] 
for i in gameword:
    score.append('_')
#print(listconv(score))

while parts > 0 and '_' in score:
    print("You have", parts, "wrong guesses left.")
    print("Available letters:", listconv(letters))
    guess = input("Please guess a letter: ")
    if guess in gameword and guess in letters:
        scoreupdate()
        letters.remove(guess)
        print("Good guess:", listconv(score))
    elif guess not in gameword and guess in letters:
        parts -= 1
        letters.remove(guess)
        print("Oops!", guess, "is not in my word:", listconv(score))
    elif guess in gameword and guess not in letters:
        print("You have already guessed that letter, please guess again.")
    else:
        print("That is not a valid guess, please try again.")
    print('')

if '_' not in score:
    print("You win! Nice job figuring out my word was", gameword)
else:
    print("You lose! The word was", gameword,", better luck next time!")
