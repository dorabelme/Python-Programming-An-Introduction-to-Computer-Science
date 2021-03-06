#rball.py
from random import random

# Pseudocode
# Print an introduction
# Get the inputs from the user: probA, probB, n
# Simulate n games of racquetball using probA and probB
# Print a report on the wins for playerA and playerB


def main():
	printIntro()
	probA, probB, n = getInputs()
	winsA, winsB = simNGames(n, probA, probB)
	printSummary(winsA, winsB)

def printIntro():
	print("This program simulates a game of racquetball between two")
	print('players called "A" and "B". The ability of each player is')
	print("indicated by a probability (a number between 0 and 1) that")
	print("the player wins the point when serving. Player A always")
	print("has the first serve.")

def getInputs():
	# Returns the three simulation parameters probA, probB and n
	a = float(input("What is the prob. player A wins a serve? "))
	b = float(input("What is the prob. player B wins a serve? "))
	n = int(input("How many games to simulate? "))
	return a, b, n

def simNGames(n, probA, probB):
	# Simulates n games of racquetball between players whose
	# abilities arre represented by the probability of winning a serve.
	# Returns number of wins for A and B
	winsA = winsB = 0
	for i in range(n):
		scoreA, scoreB = simOneGame(probA, probB)
		if scoreA > scoreB:
			winsA = winsA + 1
		else:
			winsB = winsB + 1
	return winsA, winsB

def simOneGame(probA, probB):
	# Simulates a single game or racquetball between players whose
	# abilities are represented by the probability of winning a serve.
	# Returns final scores for A and B
	scoreA = 0
	scoreB = 0
	serving = "A"
	while not gameOver(scoreA, scoreB):
		if serving == "A":
			if random() < probA: 	# A wins the serve
				scoreA = scoreA + 1
			else:					# A loses the serve
				serving = "B"
		else:
			if random() < probB:	# B wins the serve
				scoreB = scoreB + 1
			else:					# B loses the serve
				serving = "A"
	return scoreA, scoreB

def gameOver(a, b):
	# a and b represent scores for a racquetball game
	# Returns True if the game is over, False otherwise.
	return a ==15 or b==15

def printSummary(winsA, winsB):
	# Prints a summary of wins for each player.
	n = winsA + winsB
	print("\nGames simulated:", n)
	print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
	print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()





