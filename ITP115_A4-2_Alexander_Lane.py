# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Assignment 2
# Description:
# create a program that rolls a D20

# For loop to run 10 times
# print starting text
# choose case
# roll die
# compare result agianst case, win or lose

import random

def main():

    for x in range(10):
        points = 0
        # rolling D20
        d20 = random.randrange(1, 21)
        # choosing case
        case = random.randrange(1, 6)
        # print start text
        print ("You are rolling for CASE",case,"\nYou will win for the following numbers:")
        # case logic
        # case 1 wins with range(1,20,2)
        if case == 1:
            match = False
            for winNum in range(2, 21, 2):
                print (winNum, end=" ")
            print(" ")
            if d20 % 2 == 0:
                match = True
        # case 2 wins with range(1,19,3)
        elif case == 2:
            match = False
            for winNum in range(1, 20, 2):
                print (winNum, end=" ")
            print(" ")
            if (d20 + 1) % 2 == 0:
                match = True
        # case 3 wins with range(5,10)
        elif case == 3:
            match = False
            for winNum in range(5, 11):
                print (winNum, end=" ")
            print (" ")
            if d20 >= 5 and d20 <= 10:
                match = True
        # case 4 wins with range(10,20,2)
        elif case == 4:
            match = False
            for winNum in range(10, 21, 2):
                print (winNum, end=" ")
            print (" ")
            if d20 >= 10 and d20 % 2 == 0:
                match = True
        # case 5 wins with range(1,19,3)
        else:
            match = False
            for winNum in range(3, 19, 3):
                print (winNum, end=" ")
            print (" ")
            if d20 % 3 == 0:
                match = True
        #print roll notification
        print("\nNow rolling ... \nYou rolled a",d20,"!")
        # win logic
        if match == True:
            print("You won 50 points! :)\n")
            points = points + 50
        else:
            print("You didn't win :(\n")
    print("\nYour total score is:", points, "Thanks for playing!")

main()