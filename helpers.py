import random
from Peg import *

#####################################################################
## Description:  Reset colorCounts dictionary values to 0
#####################################################################
def resetColorCounts(solution,colorCounts):

	for s in solution:
		colorCounts[s.getPegVal()] = 0

#####################################################################
## Description:  Sets colorCounts of each value. Used to reset for
##				 each turn
#####################################################################
def setColorCounts(solution,colorCounts):

	resetColorCounts(solution,colorCounts)

	# Create counts of colors dictionary from solution
	for s in solution:
		colorCounts[s.getPegVal()] = colorCounts.get(s.getPegVal(),0) + 1

#####################################################################
## Description:  Returns if the values in the guess are valid 
##				 between the specified min and max values, inclusive
#####################################################################
def isValidGuess(guess,minVal,maxVal):

	# Check each value in the guess
	for val in guess:

		if val > maxVal or val < minVal:
			return False 

	return True

#####################################################################
## Description:  Returns if the user's guess was completely correct
#####################################################################
def isGuessCorrect(guess,solution):

	# Compare each peg in the guess vs the solution
	for i in range(0,len(guess)):

		if guess[i] != solution[i].getPegVal():
			return False

	return True

#####################################################################
## Description:  Determines which pegs were correct in the user's
##				 user's guess.  "X" is correct location and color.
##				 "O" is just a color color
#####################################################################
def getGuessStatus(guess,solution,results,colorCounts):

	turnResults = ["-","-","-","-"]

	# Compare each peg in the guess to the solution; complete matches
	for i in range(0,len(guess)):

		# Check if the guess is in the correct location and of the
		# correct color
		if guess[i] == solution[i].getPegVal():

			turnResults[i] = "X"

			# Update the colors already checked
			colorCounts[guess[i]] =  colorCounts.get(guess[i],0) - 1
			
	# Compare each peg in the guess to the solution; color only matches
	for i in range(0,len(guess)):	

		# Check if the guess peg is of the right color
		if isColorInSolution(guess[i],solution,colorCounts):

			if turnResults[i] == "-":
				turnResults[i] = "O"

			# Update the colors already checked
			colorCounts[guess[i]] = colorCounts.get(guess[i],0) - 1

	results.append(randomizeResult(turnResults))

#####################################################################
## Description:  Returns if a specific color exists within the 
##				 solution regardless of its position.
#####################################################################
def isColorInSolution(color,solution,colorCounts):

	# Check each peg in the solution for a matching color
	for i in range(0,len(solution)):

		if solution[i].getPegVal() == color and colorCounts.get(color,0) > 0:
			return True

	return False


#####################################################################
## Description:  Creates an array of pegs, each with a randomly
##				 assigned value
#####################################################################
def makeRandomPegs(pegs):

	# Create a random set of 4 pegs
	for i in range(0,4):

		# Get a random number from 1-6 to determine peg color; colors represented by integers
		peg = Peg(random.randint(1,6))
		pegs.append(peg)

#####################################################################
## Description:  Returns a randomly rearranged array of the result
#####################################################################
def randomizeResult(result):

	newResult = []
	randInts = [-1,-1,-1,-1]

	for i in range(0,len(result)):

		# Initialize for the while loop
		randInt = -1

		while(randInt in randInts):
			randInt = random.randint(0,3)

		randInts[i] = randInt

		newResult.append(result[randInt])

	return newResult

#####################################################################
## Description:  Prints the board game in its current state
#####################################################################
def printGameBoard(guesses,results):

	# Loop through all guesses
	for i in range(0,len(guesses)):

		outputStr = ""

		# Loop through all guesses within a guess
		for j in range(0,len(guesses[i])):

			outputStr += str(guesses[i][j])

			if j < len(guesses[i]) - 1:
				outputStr += "-"

		outputStr += " | "

		for j in range(0,len(results[i])):

			outputStr += results[i][j]

			if j < len(results[i]) - 1:
				outputStr += " "

		print("\nTurn ",i + 1,": ",outputStr,"\n")