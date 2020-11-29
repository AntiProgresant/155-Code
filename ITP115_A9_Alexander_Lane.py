# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Assignment 9
# Descripiton:
# this program reads a CSV file  with 15 languages, then asks the user to choose a language and creates a list of words in that language,
# then asks the user for a word and translates that into all 15 languages

def getLanguage(fileName):
    fileIn = open("languages.csv", "r")
    headerLine = fileIn.readline()
    headerLine = headerLine.strip()
    langList = headerLine.split(",")
    fileIn.close()
    return langList

def getSecondLanguage(langList):
    copyList = list(langList[1:])
    userChoice = ""
    userChoice = input("Enter a language: ").capitalize()
    while userChoice not in copyList:
        print("this program does not support", userChoice)
        userChoice = input("Enter a language: ").capitalize()
    return userChoice

def readFile(langList, langStr, fileName):
    langWords = []
    fileIn = open(fileName, "r")
    fileIn.readline()
    langPosition = langList.index(langStr)
    for line in fileIn:
        lineList = line.strip()
        lineList = line.split(",")
        langWords.append(lineList[langPosition])
    return langWords
    fileIn.close()

def translateWords(engList, secondList, resultsFile):
    fileOut = open(resultsFile, "w")
    continueGame = True
    while continueGame == True:
        transWord = input("Choose an english word to translate: ").lower()
        if transWord in engList:
            transPosition = engList.index(transWord)
            translation = secondList[transPosition]
            if translation != "-":
                print(transWord,"=",translation)
                print(transWord,"=",translation, file=fileOut)
            elif translation == "-":
                print ("There is no translation to",transWord)
        elif transWord not in engList:
            print("That word is not in the English list")
        continueChoice = input("\nWoud you like to enter another word? (y/n): ").lower()
        if continueChoice == "y":
            continueGame = True
        elif continueChoice == "n":
            continueGame = False
        while continueChoice != "y" and continueChoice != "n":
            continueGame = input("\nWoud you like to enter another word? (y/n): ").lower()
    fileOut.close()

def createResultsFile(language, resultsFile):
    results = open(resultsFile, "a")
    # print("Words translated from English to "+language+".")
    print("Words translated from English to "+language+".", file=results)
    results.close()

def main():
    print("Language Translator\nTranslate English words to one of the following languages:")
    print("\tDanish Dutch Finnish French German Indonesian Italian\n\tJapanese Latin Norwegian Portuguese Spanish Swahili Swedish ")
    langStr = "English"
    languageFile = "languages.csv"
    # creates list of languages
    languages = getLanguage(languageFile)
    # creates list of english words
    englishList = readFile(languages, langStr, languageFile)
    # gets the second language that user chooses
    secondLang = getSecondLanguage(languages)
    # creates a lsit of avaliable words in second language
    secondLangList = readFile(languages, secondLang, languageFile)
    # creates defaut file name
    defaultResultFile = secondLang+".txt"
    userFileName = input("\nEnter a name for the results file (enter for "+secondLang+".txt): ")
    if userFileName != "":
        print(userFileName,"\n")
        createResultsFile(secondLang, userFileName)
        translateWords(englishList, secondLangList, userFileName)

    else:
        print(defaultResultFile,"\n")
        createResultsFile(secondLang, defaultResultFile)
        translateWords(englishList, secondLangList, defaultResultFile)

main()