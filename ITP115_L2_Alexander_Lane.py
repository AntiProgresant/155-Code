# Lane Alexander
# ITP, Fall 2020
# Lab 2 Simple Barista Control

def main():
    # Ask What Size Coffee (S, M, L)
    coffeeSize = input("What size would you like (S, M, L)?: ")
    if coffeeSize.capitalize() == "S":
        coffeeSize = "small"
    elif coffeeSize.capitalize() == "M":
        coffeeSize = "medium"
    elif coffeeSize.capitalize() == "L":
        coffeeSize = "large"

    # Ask waht temp (in Degrees)
    coffeeTemp = int(input("What temperature (Farenheit) would you like?: "))
    if coffeeTemp >= 90:
        coffeeTemp = "hot"
    else:
        coffeeTemp = "iced"

    # Ask Type of beans / blend
    coffeeBean = input("What kind of beans would you like?: ")

    # Ask room for cream (y/n)
    coffeeRoom = input("would you like room for cream (y/n)?: ")
    if coffeeRoom == "y":
        coffeeRoom = "with"
    else:
        coffeeRoom = "without"

    # "You ordered a (drink) (temp) (Blend) (with/without) for cream"
    print ("You ordered a",coffeeSize,coffeeTemp,coffeeBean,"coffee",coffeeRoom,"room for cream")

main()