# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Assignment 5, Part 1
# Description:
# Create a program the randomly jumbles a string and lets the user guess the word

# select a word form the list
# create a jumbled version of the word and display to user
# have user guess until they get it correct
    # count the number of guesses it takes

import random

def main():
    play = True
    while play == True:

        wordList = ["apple", "coat", "airplane"]
        randWord = random.choice(wordList)
        jumbledWord = ""
        characterList = []
        tries = 0

        # adds each character of randword to an empty list
        for character in randWord:
            characterList.append(character)
        # Removes characters from character list and adds them to the jumbled word string
        while len(characterList) > 0:
            randomLetter = random.choice(characterList)
            characterList.remove(randomLetter)
            jumbledWord = jumbledWord + randomLetter
        # first print statement
        print ("\n The jumbled word is", jumbledWord,"\n")
        # While the answer is correct
        correct = False
        while correct == False:
            guess = input("Please enter your guess: ").lower()
            if guess.lower() == randWord:
                print ("\nYou're right!\n")
                if tries > 0:
                    print ("It took you",tries,"tries\n")
                correct = True
            else:
                tries = tries +1
                print("\nTry again\n")
                print("Numbers of tries:", tries, "\n")
        playAgain = input("Would you like another word? (y/n)\n>").lower()
        if playAgain == "y":
            play = True
        else:
            play = False
            print("See you later!")
main()