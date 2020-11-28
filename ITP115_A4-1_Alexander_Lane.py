# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Assignment 2
# Description:
# Counts the number of times a character appears in a user input sentence

# User input a sentence
# Look at every letter in the sentenceand count how many times each letter of the alphabet appears
# count how many times special characters appear
# Print each letter followed by the number of asterik for how many times it appears in the sentence
    # if letter never appeared print none

def main():
    alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # alphabetList = "abcdefghijklmnopqrstuvwxyz"
    letterCount = 0
    specialCount = 0
    stars = "*"

    # take in input
    userSentence = input("Please enter a sentence: ").lower()
    # print the text line
    print ("\nthis is the character distribution")
    # count special characters
    for special in userSentence:
        # excluding spaces
        if special != " ":
            if special not in alphabetList:
                specialCount = specialCount + 1
    # count letters in alphabet
    print ("Special Characters:", (stars * specialCount))
    for character in alphabetList:
        for letter in userSentence:
            if character == letter:
                letterCount = letterCount + 1
        # if there are none of the letters
        if letterCount == 0:
            print(character,":NONE")
        else:
            print (character,":",(stars * letterCount))
        letterCount = 0
main()