# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Assignment 2
# Description:
# make a program that stores user input, then displays the largest, smallest and average number



def main():
    # Restart conditions
    playAgain = True
    reply = ""

    # first while statement
    while playAgain is True:

        # Establishing variables
        entryNum = 0
        maxNum = 0
        minNum = 999999
        sum = 0
        counter = 0

        # asking for first user input
        entryNum = int(input("Input an integer greater than or equal to 0 (-1 to quit)\n> "))

        # second while statement
        while entryNum != -1:
            if entryNum < minNum:
                minNum = entryNum
            elif entryNum > maxNum:
                maxNum = entryNum
            # Exiting if loop, adding counter and calculating sum
            sum = sum + entryNum
            counter = counter + 1
            # asking for entry number within loop
            entryNum = int(input("> "))
        # Exiting loop and performing calculations
        averageNum = (sum / counter)
        print("maximum", maxNum)
        print("minimum is", minNum)
        print("The Average is", averageNum)
        # Asking if you want to restart
        reply = input("\nWould you like to start agian? (y/n): ").lower()
        if reply == "y":
            playAgain = True
        elif reply == "n":
            playAgain = False
            print("Thanks for Playing!")
        else:
            while reply != "y" and reply != "n":
                reply = input("Please enter y or n: ").lower()
                if reply == "n":
                    playAgain = False
                    print ("Thanks for Playing!")
main()