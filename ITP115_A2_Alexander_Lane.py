# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Assignment 2
# Description
# this program creates a harry potter vending machine
# It determines change and gives a discount.

# Write a program that calculates vending change in harry potter currency
# Work with Numeric Calculations
# Work with basic conditionals (if/elif/else)

def main():
    galleon = 493
    sickle = 29
    knut = 1
    totalChange = ""
    sickleChange = ""
    exactChange = ""
    coupon = ""
    item = ""
    itemPrice = ""
    butterbeer = 58
    quill = 10
    dailyProphet = 7
    bookSpells = 400
    # display options and costs. Allow suggestion
    choice = input("Please select an item from the vending machine: \n\ta) Butterbeer: 58 knuts \n\tb) Quill: 10 knuts \n\tc) The Daily Prophet: 7 knuts \n\td) Book of Spells: 400 knuts \n>").lower()
    if choice == "a":
        item = butterbeer
        itemPrice = 58
    elif choice == "b":
        item = quill
        itemPrice = 10
    elif choice == "c":
        item = dailyProphet
        itemPrice = 7
    elif choice == "d":
        item = bookSpells
        itemPrice = 400
    else:
        item = butterbeer
        print ("Invalid choice... but enjoy your Butterbeer!")
    # share on insta?
    discount = input("Would you like to share on Instagram for a 5 knut discount? (y/n): ").lower()
    if discount == "y":
        coupon= 5
    elif discount == "n":
        coupon = 0
    else:
        print("Invalid input... No Coupon for you!")
        coupon = 0
        # always skips to else?
    # How many Galleons would you like to use
    numGalleons = int(input("\nHow many Galleons are you depositing?: "))
    payment = (493 * numGalleons)
    # calculating the total change
    totalChange = payment - item - coupon
    # Calculating the exact change
    sickleChange = totalChange // sickle
    exactChange = (totalChange % sickle)
    # printing their order
    print ("You bought a",item,"for",itemPrice,"knuts (with a coupon of",coupon,"knuts) and paid with one galleon\nhere is your change (",totalChange,") knuts")
    print ("Sickles:",sickleChange,"\nKnuts:",exactChange)
main()