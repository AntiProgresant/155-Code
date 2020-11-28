# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Assignment 5, Part 2
# Description:
# Write a program that prompts the user for the shift value (e.g. 3) and then a plain-text message to encode.
# encrypt and print, then decrypt and compare the decrypted message with the original

def main():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    originalWord = input("enter a message: ").lower()
    encryptShift = int(input("\nEnter a number to shift by (0-25): "))
    cipher = []
    specialCharacter = ""
    print ("Encrypting message...")
    # shifts everything down by encryptShift number
    for character in alphabet:
        cipher.append(alphabet[(alphabet.index(character) + encryptShift) % 26])
    # encrypted phrase as a string
    encryption = ""
    for character in originalWord:
        if character in alphabet:
            if character.isalpha():
                encryption = encryption + cipher[alphabet.index(character)]
        else:
            encryption = encryption + character
    print ("\nEncrypted message: ", encryption)
    # Decryption
    decryption = ""
    for character in encryption:
        if character in alphabet:
            decryption = decryption + alphabet[cipher.index(character)]
    # print encrypted and decryption
    print ("\nDecrypted:",encryption)
    print ("Original:",originalWord)
main()