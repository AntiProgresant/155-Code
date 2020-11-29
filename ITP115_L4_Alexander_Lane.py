# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Lab 4

# Using a while loop, ask user for an english word
# translate word to elvish with for
# dislpay translation
# ask for another word
    # if yes, ask for another word
    # if no, print goodbye in elvish

import random

def main():

    # while loop conditions
    playAgain = True
    translation = False
    print("Welcomeo toen theen Pigen Elvisha Translatore!\n (Welcome to the Pig Elvish translator!)")

    while playAgain is True:

        # declaring variables
        engword = ""
        fullTranslation = ""
        randVowel = random.choice("aeiou")
        engWord = input("Please enter a word you want to translate: ")
        # translating the word
        while translation is False:
            wordLen = len(engWord)
            if wordLen >= 4:
                engWord = engWord + randVowel
            elif wordLen <= 3:
                engWord = engWord + "en"
            # changing letters
            for letter in engWord:
                if letter == "c":
                    fullTranslation = fullTranslation + "k"
                else:
                    fullTranslation = fullTranslation + letter
            # printing and resetting
            print(fullTranslation)
            translation = True
            playAgain = False
        # asking for another word
        repeat = input("would you like to translate another word? (y/n): ").lower()
        if repeat == "y":
            playAgain = True
            translation = False
        elif repeat == "n":
            playAgain = False
            print("Goodbyea! Havea aen nicee dayne!\nGoodbye! Have a nice day!")
main()