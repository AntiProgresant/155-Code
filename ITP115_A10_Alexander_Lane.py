# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Description
# Create a program the simulates a user's music library. importing a library, saving changes to the file
# Library will be represented as a dictionary. Keys are the artist's names(strings), and values are a list of albums by the artist

import MusicLibraryHelper
import random

def displayMenu():
    print("Welcome to Your Music Library")
    print("Options:\n\t1) Display library\n\t2) Display all artists\n\t3) Add an album\n\t4) Delete an album\n\t5) Delete an artist\n\t6) Search library\n\t7) Generate a random playlist\n\t8) Make your own playlist\n\t9) Exit ")

def displayLibrary(musicLibDictionay):
    # for every artist in the library
    for key in musicLibDictionay:
        # print the artist and their albums
        print("\nArtist:",key)
        print("Albums:")
        # for every album in list, print the album
        for i in musicLibDictionay[key]:
            print("\t-",i)

def displayArtists(musicLibDictionary):
    print("Displaying all Artists")
    # for every artist in the library print the artist
    for key in musicLibDictionary:
        print("-",key)

def addAlbum(musicLibDictionary):
    # get user input
    artistChoice = input("Enter the artist: ").title()
    albumChoice = input("Enter an Album: ").title()
    # if the artist is in the library
    if artistChoice in musicLibDictionary:
        # if the album is not in the artist's list
        if albumChoice not in musicLibDictionary[artistChoice]:
            # add the album to the artist's list
            musicLibDictionary[artistChoice].append(albumChoice)
    # if the artist is not in the library
    elif artistChoice not in musicLibDictionary:
        # add a key-value for the artist and album
        musicLibDictionary[artistChoice] = [albumChoice]

def deleteAlbum(musicLibDictionary):
    # get user input
    artistChoice = input("Enter the artist: ").title()
    albumChoice = input("Enter an Album: ").title()
    # if the artist is in the library
    if artistChoice in musicLibDictionary:
        # if the album is in the artist's album list
        if albumChoice in musicLibDictionary[artistChoice]:
            # remove the album from the album list
            musicLibDictionary[artistChoice].remove(albumChoice)
            # if the length of the album list is 0, remove the artist
        if len(musicLibDictionary[artistChoice]) == 0:
            del musicLibDictionary[artistChoice]
            return True
        if albumChoice not in musicLibDictionary[artistChoice]:
            return False
    elif artistChoice not in musicLibDictionary:
        return False

def deleteArtist(musicLibDictionary):
    delArtistChoice = input("Enter the artist: ").title()
    if delArtistChoice in musicLibDictionary:
        del musicLibDictionary[delArtistChoice]
        return True
    elif delArtistChoice not in musicLibDictionary:
        return False

def searchLibrary(musicLibDictionary):
    # Creating empty Lists
    artistResults = []
    albumResults = []
    # user input
    searchTerm = input("Please enter a search term: ").title()
    # for each artist in the library
    for key in musicLibDictionary:
        # if the search term is in the artist name
        if searchTerm in key:
            # add artist name to artist result list
            artistResults.append(key)
        # for each album in the artist's album list
        for i in musicLibDictionary[key]:
            # if the search term is in the album name
            if searchTerm in musicLibDictionary[key]:
                # add album to album results list
                albumResults.append(i)
    # artists
    print("Artist containing '"+searchTerm+"'")
    # if the length of the artist results list is 0 print no results
    if len(artistResults) == 0:
        print("No Results")
    # if the length of the artist reslults list is not 0
    elif len(artistResults) != 0:
        # for each artist in artist results, print the artist
        for i in artistResults:
            print("\t-",i)
    # albums
    print("Albums Containing '"+searchTerm+"'")
    # if album results is 0, print no results
    if len(albumResults) == 0:
        print("No Results")
    # if album results list is more than 0
    elif len(albumResults) != 0:
        # for every album result print the album name
        for i in albumResults:
            print("\t-",i)

def generateRandomPlaylist(musicLibDictionary):
    print("Here is your random playlist.")
    for key in musicLibDictionary:
        randomAlbum = random.choice(musicLibDictionary[key])
        print(randomAlbum+" by "+key)

def main():
    # while loop condition and importing music library file
    isRunning = True
    library = MusicLibraryHelper.loadLibrary("musicLibrary.dat")
    # while the program is runnig
    while isRunning is True:
        displayMenu()
        menuChoice = int(input("> "))
        # display Library
        if menuChoice == 1:
            displayLibrary(library)
        # display artists
        elif menuChoice == 2:
            displayArtists(library)
        # add album
        elif menuChoice == 3:
            addAlbum(library)
        elif menuChoice == 4:
            deleteAlbum(library)
        # delete Album
        elif menuChoice == 5:
            deleteArtist(library)
        # Search library
        elif menuChoice == 6:
            searchLibrary(library)
        # create a random playlist
        elif menuChoice == 7:
            generateRandomPlaylist(library)
        #elif menuChoice == 8:
        # Exit the program
        elif menuChoice == 9:
            print("Saving music library...\nGoodbye!")
            MusicLibraryHelper.saveLibrary("musicLibrary.dat:", library)
            isRunning = False
main()