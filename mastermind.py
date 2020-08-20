##################################################################### 
## CS325 Analysis of Algoirthms
## Program name: HW6 - Portfolio Assignment (Option 1) - Mastermind
## 
## Author: Pavel Gordeyev
## Date: 8/9/20
## Description: Text-based version of the mastermind game. User will
##				have 8 turns to guess the color and sequence of 4
##				pegs. Peg colors are represented by numbers 1-6.
##				Each turn, they will receive feedback on the 
##				correctness of the guess that was played.
##				An "X" means that it is an exact match for color
##				and location, while a "O" is only a match for color.
##				The results are in a random order.
#####################################################################

import re
from helpers import *

#####################################################################
## Description:  Performs the gameplay for the Mastermind game
#####################################################################
def main():

	# Display welcome message
	welcome = "Welcome to Mastermind!!!\nIn this game, you will attempt to find the correct color and sequence of 4 pegs.\nYou will have 8 guesses to try and guess the solution and win the game!\nEach turn, we will show either a white dot, represented by a O signifying \nthat one of the pegs is the correct color but in the wrong location,\nor a black dot, represented by an X signifying that one of the pegs is in\nthe correct location and is of the correct color. \nThe order of the results, which follow the '|', are in no particular order.\n\n Enter /q to quit at anytime"

	print("\n",welcome,"\n\n")

	# Create random peg selection
	solution = []
	makeRandomPegs(solution)

	# Initialize dictionary to store counts of colors in solution
	colorCounts = dict()

	# Initialize an array for the player's turns
	guesses = []

	# Initialize an array for each guesses results
	results = []

	# Initialize winning boolean
	won = False

	# Allow player to make 8 guesses
	for turn in range(0,8):

		# Validate user input
		while(1):

			# Ask user for a guess; convert to integer array
			guess = input("Enter your guess(4 Values from 1-6 ONLY;ex. 1 2 3 4): ")

			if guess == "/q":
				print("Ok, see you next time!")
				exit()
			elif not re.match('^[0-9\s]*$',guess.rstrip()): # Matches numbers and spaces only
				print("Invalid entry!")
			else:
				guess = list(map(int,guess.split()))

				if len(guess) < 4:
					print("\nNot enough values were entered. Please enter 4 values!\n")
				else:
					if not isValidGuess(guess,1,6):
						print("\nOne of the guessed pegs is not a valid value! Please try again!\n")
					else:
						break

		# Add to list of guesses
		guesses.append(guess)

		# Check if user's guess is completely correct
		if not isGuessCorrect(guess,solution):

			# Reset color counts
			setColorCounts(solution,colorCounts)

			# Get the status of how correct the guess was
			getGuessStatus(guess,solution,results, colorCounts)

			# Print out board with results all turns with white and black pegs
			printGameBoard(guesses,results)

		else: # Player won the game
			print("\nCongrats! You got it right! The solution was: ",guess)
			won = True
			break

	if not won:
		# Solution was not found by the user after 8 turns
		print("\nYou ran out of turns! Please try again next time!\n")



# Call main function
if __name__ == "__main__":
	main()

