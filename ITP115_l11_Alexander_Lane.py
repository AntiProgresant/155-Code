# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Lab 11

import random

# creating Die object
class Die(object):
    def __init__(self, numSides = 6):
        self.numSides = numSides
        self.rollValue = 0
    # Roll method
    def roll(self):
        rollValue = random.randrange(1, self.numSides+1)
        return(rollValue)
    # how informaitno is displayed
    # def __str__(self):
        # msg = ("Die has",self.numSides,"sides and rolled",self.rollValue)
        # return msg

def calculateSum(die1, die2):
    # adding the sum of dice passed through
    sum = die1 + die2
    return sum

def main():
    # Dice one
    useDefaultSides1 = input("Would you like to use the default number of sides for the first die (y/n)?: ").lower()
    if useDefaultSides1 == "y":
        dice1 = Die()
    elif useDefaultSides1 == "n":
        useSides1 = int(input("How many Sides?"))
        dice1 = Die(useSides1)
    # Dice two
    useDefaultSides2 = input("Would you like to uyse the default number of sides for the second die (y/n)?: ").lower()
    if useDefaultSides2 == "y":
        dice2 = Die()
    elif useDefaultSides2 == "n":
        useSides2 = int(input("How many Sides?"))
        dice2 = Die(useSides2)

    # how many rolls
    timesRolled = int(input("How many times do you want to roll the die?: "))
    for i in range(timesRolled):
        roll1 = dice1.roll()
        roll2 = dice2.roll()
        print("Dice 1 rolled a",roll1)
        print("Dice 2 rolled a", roll2)
        diceSum = calculateSum(roll1, roll2)
        print("The sum of dice1 and dice 2 is",diceSum)

main()