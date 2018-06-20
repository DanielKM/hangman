"""
Created on Sat May 26 12:18:47 2018
Edited on Mon May 28 04:42:32 2018
@author: daniel
"""

import random 

"""
welcoming the user
"""
name = input("Hello Traveler! What is your name? ")
print("\nHello, " + name + "! Time to play some hangman. You start with 8 guesses!")
print(" ")

"""
here we set the secret word
"""
word = ['bill','delightful','chaotic','pious','capitulate','ferocious','indigenous','nerd','secret',
        'feces', 'figure', 'rites', 'daughter', 'violence','blizzard','AWESOME','truncate','tempest',
		'barbecue', 'fullsome', 'chair', 'table', 'bench', 'dryer', 'washer', 'shoes', 'computer',
		'shark','volcano','fireball','hurricaine','tirade','rage','medication', 'instruction']

def chooseWord(word):
    """
    word (list): list of words (strings)

    Returns a word from wordlist at random
    """

    secretWord = random.choice(word)
    return secretWord

def hangman(secretWord):
    """
    secretWord (string): the randomly chosen string from function word

    introduces a game of hangman
    """
    print("The word is " + str(len(secretWord)) + " letters long. Start guessing...")

    guesses = ''
    turns = 8

    while turns > 0:         
        failed = 0             
        for char in secretWord:      
            if char in guesses:    
                print(" " + char, end="") 

            else:
                print(" _", end="")
                failed += 1    

        if failed == 0:        
            print("\nYou won, Hangman goes free!")  
            break
        
        guess = input("\nGuess a letter:") 
        guesses += guess                    

        if guess not in secretWord:  
            turns -= 1        
            print("That is incorrect.")
            if turns == 0:           
                print("You lose! Not as bad as Hangman does though!")
            else:
                print("You have " + str(turns) + ' more guesses until Hangman dies!' )

"""
calls secretWord function and hangman function
"""                

while True:
    secretWord = chooseWord(word).lower()
    hangman(secretWord)
    restart = input('Would you like to play again? y or n?')
    if restart == 'n':
        break
    elif restart == 'y':
        continue