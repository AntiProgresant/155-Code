# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Lab 9

def read_file(user_genre, file_name):
    finalList = []
    fileIn = open(file_name, "r")
    for line in fileIn:
        line = line.strip()
        if user_genre in line:
            showList = line.split(",")
            finalList.append(showList[0])
    fileIn.close()
    return finalList

def write_file(genre, show_list):
    fileOut = open(genre+".txt", "w")
    print (show_list, file = fileOut)
    fileOut.close()

def main():
    genreList = ["action & adventure", "animation", "comedy", "documentary", "drama", "mystery & suspense", "science fiction & fantasy"]
    fileName = "shows.csv"
    goodPick = False
    print ("TV Shows\nPossible genres are action & adventure, animation, comedy, documentary, drama, mystery & suspense, science fiction & fantasy")
    while goodPick == False:
        userGenre = input("please pick one of the genres: ").lower()
        if userGenre in genreList:
            goodPick = True
    showRecs = read_file(userGenre, fileName )
    write_file(userGenre, showRecs)
    print ("the file '"+userGenre+"'.txt has the following shows:\n",showRecs)
main()