# Lane lexander, ljalexan@usc.print
#ITP 115, Fall 2020
# Lab 8

import random

def coin():
	coinFlip = random.randrange(1,3)
	if coinFlip == 1:
		heads = "Heads"
		return heads
	elif coinFlip == 2:
		tails = "Tails"
		return tails

def experiment():
	headCount = 0
	flips = 0
	while headCount != 3:
		result = coin()
		if result == "Heads":
			headCount += 1
			flips += 1
		else:
			headCount = 0
			flips += 1
	return flips
	

def main():
	experimentNum = 0
	sum = 0
	while experimentNum < 10:
		flipCount = experiment()
		sum = sum + flipCount
		experimentNum = experimentNum + 1
	average = (sum/10)
	print ("The average for 3 heads in a row is:",average)
main()