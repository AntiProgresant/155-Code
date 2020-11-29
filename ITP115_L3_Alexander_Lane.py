# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Lab 3

# Write a program that uses a while loop to produce a triangle
# Triangle should be 10 lines tall
# to center the riangle, include initial spaces on each line
# bottom row has 19 ^ symbols
# between every ^ is a single space
# Hint 1: use * to repeat strings
# Hint 2: need at least 1 while loop to control how many rows print, need numSpaces counter and numSymbols counter

def main():

    row = 1
    rowNum = 10
    numSpaces = 19
    numSymbols = 1
    symbol = " ^"
    outsideSpace = " "

    while row <= rowNum:
        print ((outsideSpace * numSpaces),(symbol * numSymbols))
        numSpaces = numSpaces - 2
        numSymbols = numSymbols + 2
        row = row + 1
main()