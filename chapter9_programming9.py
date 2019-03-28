# function inputs: init_hand
# set hand to init_hand and hasAce to False
# while hand is less than 17
	# randomly select card
	# if card is Ace through 10
		# add value of card to hand
		# if card is Ace
			# set hasAce to true
	# otherwise
		# add 10 to hand
	# if hasAce and 17 <= hand + 10 <= 21
		# add 10 to hand
# if hand busts
	# retrn true
# otherwise
	# return false

from random import randrange

def main():
	printIntro()
	n, init_hand = getN()
	busts = simNGames(n, init_hand)
	printProb(busts, n, init_hand)

def printIntro():
	print("This program simulates the dealer's hand in a game of Blackjack")
	print("played by multiple times and returns an estimate of the probability")
	print("of a bust in any one game.")

def getN():
	n = eval(input("Enter the number of games to stimulate: "))
	usr_in = input("Enter the starting value of the dealer's hand or " +
			"help for more info: ")
	if usr_in.lower() == "help":
		print("This program returns the probability of a bust given the")
		print("dealer's initial face-up card")
		print("For the probability when the dealer is showing an Ace through")
		print("10, enter the corresponding value from 1 - 10.")
		print("For the probability when the dealer is showing a face card")
		print("enter 10.")
		usr_in = input("Enter the starting value of the dealer's hand")
	init_hand = eval(usr_in)
	return n, init_hand

def simNGames(n, init_hand):
	busts = 0
	for i in range(n):
		if bustOneGame(init_hand):
			busts += 1
	return busts

def bustOneGame(init_hand):
	hand = init_hand
	hasAce = False 
	while hand < 17:
		card = randrange(1,14)
		if 1 <= card <= 10:
			hand += card
			if card == 1:
				hasAce = True 
		else:
			hand += 10
		if hasAce and 17 <= hand + 10 <= 21:
			hand += 10
	if hand > 21:
		return True 
	return False 

	
def printProb(busts, n, init_hand):
	prob = busts / n
	print("\nDealer's Initial Hand Showing:", init_hand, "Point(s).")
	print("\nEstimated Probability of a Bust: {0:.1%}".format(prob))

if __name__ == '__main__':
	main()


