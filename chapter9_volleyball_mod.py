
from random import random


def getStats(probA, probB, n):
	winsA, winsB = simNGames(n, probA, probB)
	return winsA, winsB

def simNGames(n, probA, probB):
	# Simulates n games of volleyball between players whose
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
	# Simulates a single game or volleyball between players whose
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
	# a and b represent scores for a volleyball game
	# Returns True if the game is over, False otherwise.
	return (a >=15 or b >=15) and abs(a-b)>= 2






