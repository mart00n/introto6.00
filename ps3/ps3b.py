#! /usr/bin/env python
# 6.00 Problem Set 3B Solutions
# 
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Andrew Marton
# Started at 1000

from ps3a import *
import time
from perm import *

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
    word_scores = {} # Makes blank dict to record all the valid words and their score
    #print('Sanity check!')
    print('Thinking...')
    for n in range(1, HAND_SIZE + 1):
        permlist = get_perms(hand, n)
        if len(permlist) == 0:
            return 0
        for word in permlist:
            if is_valid_word(word, hand, word_list):
                #print(word, get_word_score(word, HAND_SIZE))
                word_scores.update({word: get_word_score(word, n)})
            elif len(permlist) == 0:
                return 0
    scores = list(word_scores.values())
    words = list(word_scores.keys())
    #print(words[scores.index(max(scores))])
    #print(type(words[scores.index(max(scores))]))
    return words[scores.index(max(scores))]
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
    print('CPU Turn')
    CPU_score = 0
    choice = ''
    #CPU_hand = deal_hand(HAND_SIZE)
    while calculate_handlen(hand) > 0: #choice != 0:
        display_hand(hand)
        choice = comp_choose_word(hand, word_list)
        if choice == 0:
            print('The computer cannot play remaining letters')
            break
        #print(choice)
        #print(type(choice))
        CPU_score += get_word_score(choice, calculate_handlen(hand))
        hand = update_hand(hand, choice) # Handles the list returned by word choice fxn
        print('CPU plays', "'",choice,"'", 'worth', get_word_score(choice, calculate_handlen(hand)), 'points') 
    print('CPU hand completed!') 
    if calculate_handlen(hand) == 0:
        print('All letters used, 50 bonus points!')
    print('Total score:', CPU_score)

#
# Problem #6C: Playing a game
#
#
def CPU_play_game(word_list):
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
    pick = ''
    while pick != '.':
        print('Main menu - type 1 for solo game, 2 for the CPU to play, and . to quit')
        pick = input('...')
        if pick == '1':
            single_player_game(word_list)
        elif pick == '2':
            comp_play_hand(deal_hand(HAND_SIZE), word_list)
        elif pick == '.':
            print('Program closing...')
            exit()
        else:
            print('Invalid selection')


    # The organization above is stupid and I'm doing my own thing
    # 2 comes first, funnels to two game logic functions - one for a CPU vs match 1 for human
    # Repeating hands is dumb and who cares, this project is too big anyhow...

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    CPU_play_game(word_list)
    #hand = deal_hand(HAND_SIZE)
    #hand = get_frequency_dict('figures')
    #comp_choose_word(hand, word_list)
    #comp_play_hand(hand, word_list)

    
