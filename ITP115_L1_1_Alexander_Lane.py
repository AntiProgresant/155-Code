# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Lab 1
# Description: working with print functions

# Where work wil take place
def main():
    # [1] print a box
    print (" _")
    print ("| |")
    print ("| |")
    print ("|_|\n\n")

    # [2] Monty Python quote
    print ("You don't frighten us, English pig-dogs! \nGo and boil your bottoms, sons of a silly person! \n\t-\"Monty Python and the Holy Grail\"\n\n")

    # [3] User Generated Calendar
    month = input("What month are we in?: ")
    dayName = input("What day is it?: ")
    dayNumber = input("What day of the month is today?: ")
    num2 = 1                                                                    # must declare this before using in dayNext function
    dayNext = int(dayNumber) + num2                                             # I was getting a lot of concatentation errors (origionally used + to join strings and variables), decided to use a variable make dayNext into a function

    print ("Today is", dayName.capitalize(), month.capitalize(), dayNumber, "and Tomorrow will be", month.capitalize(), dayNext)
main()

# Using commas instead of "+" helps to avoid concatentation errors!
# Use of string method to always output a capitalized string for months and days
# Limit of this program would be if the day entered was the last day of the month, it would only display the month entered and add 1 more day to 30 or 31