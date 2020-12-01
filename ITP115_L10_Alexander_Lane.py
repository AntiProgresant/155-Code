# Lane Alexander, ljalexan@usc.edu
# ITP 115, Fall 2020
# Lab 10

def readFile(fileName):
    fileIn = open(fileName,"r")
    wordList = []
    appearanceList = []
    wordDict = {}
    lineNum = 1
    for line in fileIn:
        # edits the lines, turns words into lists
        line = line.strip()
        line = line.strip(",.;:?'")
        wordList = line.split(" ")
        # lowercases and strips all words, adds them to the empty dictionary
        for word in wordList:
            word = word.lower()
            word.strip(",.;:?'")
            if word not in wordDict:
                wordDict[word] = [lineNum]
                # if "" delete the "" key and value
                if word == "":
                    del wordDict[""]
            else:
                wordDict[word].append(lineNum)
        lineNum = lineNum + 1
    fileIn.close()
    return wordDict

def sortKeys(dicitonary):
    # turns dictionary keys into a list and sorts
    keyList = list(dicitonary.keys())
    keyList.sort()
    return keyList

def main():
    # calls filename
    textFile = "story.txt"
    # creates dictionary
    wordDictionary = readFile(textFile)
    # creates sorted key list
    sortedDictionaryKeys = sortKeys(wordDictionary)
    print("Here is the condordance for the file 'story.txt'")
    # prints key and concordance
    for key in sortedDictionaryKeys:
        print(key+":", wordDictionary.get(key))
main()