# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Lab 6
# write a program that takes two words or statements and checks if the words are anagrams (same letters and length)
# check if each word is a palindrome (same backwards and forwards)

# ask for user input
# turn each string into a list
# if first list and second list have same length
    # sort
    # if firstList and secondList have same values
        # anagram or not
# if reversed list values and index == regular list values and index

def main():

    # establishing strings
    firstWord = input("Enter the first word: ").lower()
    secondWord = input("Enter the second word: ").lower()

    # copy of strings
    firstCopy = firstWord
    secondCopy = secondWord
    # creating base lists from strings
    firstList = list(firstWord)
    secondList = list(secondWord)
    # copy of base for sorting
    sortFirst = list(firstList)
    sortSecond = list(secondList)
    # copy of base for reversing
    revFirst = list(firstList)
    revSecond = list(secondList)
    revFirst.reverse()
    revSecond.reverse()


    # anagram
    # If the two words have the same length, sort lists
    if len(firstList) == len(secondList):
        sortFirst.sort()
        sortSecond.sort()
        # check if lists have the same values, print messages
        if sortFirst == sortSecond:
            print ("The two words are anagrams!")
    else:
        print ("The two words aren't anagrams.")

    # palindrome

    # strip strings
    stripFirst = firstCopy.strip(" ")
    stripSecond = secondCopy.strip(" ")
    # make stripped strings a list
    stripList1 = list(stripFirst)
    stripList2 = list(stripSecond)
    # reversing stipped lists
    stripList1.reverse()
    stripList2.reverse()

    # first word palindrome check
    if revFirst == stripList1:
        print ("The first word is a palindrome!")
    else:
        print ("The first word is NOT a palindrome.")
    # second word palindrome check
    if revSecond == stripList2:
        print("The second word is a palindrome!")
    else:
        print("The second word is NOT a palindrome.")
main()