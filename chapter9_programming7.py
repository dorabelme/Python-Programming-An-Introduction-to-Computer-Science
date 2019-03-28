# print an explanation of the program
# get the number of games to simulate from the user
# simulate n games of craps
# print the probability of winning

# SIMULATE N GAMES
# function inputs: n
# initialize wins to 0
# loop n games
	# simulate a single game
	# if the game is results in a win
		# add 1 to wins
	# return wins

# SIMULATE A GAME
# simulate the sum of 2 rolled dice
# if the roll is 2, 3, or 12
	# return false
# if the roll is a 7 or 11
	# return true
# otherwise
	# initialize next_roll to 0
	# while next_roll is not equal to roll or 7
		# roll again
	# if next_roll equals roll
		# return true
	# otherwise
		# return false

from random import randrange

def main():
	printIntro()
	n = getN()
	wins = simNGames(n)
	printData(wins, n)

def printIntro():
	print("This program simulates a game of craps played multiple times and")
	print("returns an estimates of the probability of winning in any one game.")

def getN():
	n = eval(input("Enter the number of games to stimulate: "))
	return n

def simNGames(n):
	wins = 0
	for i in range(n):
		if winOneGame():
			wins += 1
	return wins

def winOneGame():
	roll_1 = randrange(1,7) + randrange(1,7)
	if roll_1 == 2 or roll_1 == 3 or roll_1 == 12:
		return False 
	elif roll_1 == 7 or roll_1 == 11:
		return True 
	else:
		roll = 0
		while roll != roll_1 and roll != 7:
			roll = randrange(1,7) + randrange(1,7)
		if roll == roll_1:
			return True 
		else:
			return False 

def printData(wins, n):
	prob = wins / n
	print("\nEstimated Probability of Winning: {0:.1%}".format(prob))

if __name__ == '__main__':
	main()


