# function inputs: none
# initialize hand to 0 and hasAce to false
# while hand < 17
	# randomly select a card
	# if the card is an Ace or a 2 through 10
		# add the value of the card to hand
		# if the card is an Ace
			# set hasAce to True
	# otherwise
		# add 10 to hand
	# if hasAce is true and 17 <= hand + 10 <= 21
		# add 10 to hand
# if hand is greater than 21
	# return True
# otherwise
	# return False


from random import randrange

def main():
	printIntro()
	n = getN()
	busts = simNGames(n)
	printProb(busts, n)

def printIntro():
	print("This program simulates the dealer's hand in a game of Blackjack")
	print("played by multiple times and returns an estimate of the probability")
	print("of a bust in any one game.")

def getN():
	n = eval(input("Enter the number of games to stimulate: "))
	return n

def simNGames(n):
	busts = 0
	for i in range(n):
		if bustOneGame():
			busts += 1
	return busts

def bustOneGame():
	hand = 0
	hasAce = False 
	while hand < 17:
		card = randrange(1,14)
		if 1 <= card <= 10:
			hand += card
			if card == 1:
				hasAce = True 
		else:
			hand += 10
	if hand > 21:
		return True 
	return False 

	
def printProb(busts, n):
	prob = busts / n
	print("\nEstimated Probability of a Bust: {0:.1%}".format(prob))

if __name__ == '__main__':
	main()


