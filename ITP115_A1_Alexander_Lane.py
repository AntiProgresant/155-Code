# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Description: Creating a madlib story using variables, store user input, and then print the output information

def main():

    # Get input for variables
    firstAnimal = input("Enter an animal: ")
    secondAnimal = input("Enter another animal: ")
    firstAdj = input("Enter an adjective: ")
    firstVerb = input("Enter a verb: ")
    ingVerb = input("Enter a verb ending in 'ing': ")
    firstNum = int(input("Enter a number: "))
    secondNum = int(input("Enter a second number: "))
    thirdNum = int(input("Enter a third number: "))
    deciNum = float(input("Enter a number with a decimal: "))

    # Print command
    print ("Today, the zoo displayed",firstNum, firstAnimal,"babies.","Each",firstAnimal,"gets",deciNum,"in the",ingVerb,"area, and",secondNum,"bananas when they get",firstAdj + ".","They like to",firstVerb,"on branches, but everyone likes to watch the", secondAnimal,"when it starts",ingVerb + ".","The zoo only has",thirdNum,"of them but they escape at least",secondNum,"times a month.")

main()