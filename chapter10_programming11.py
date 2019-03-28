from random import randrange

class Card():

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def getRank(self):
		return self.rank

	def getSuit(self):
		return self.suit

	def BJValue(self):
		if self.rank <= 10:
			return self.rank
		else: 
			return 10


	def __str__(self):

	# set ranks equal to a list containing the names of each rank
	# set suits equal to al ist containing the names of each suit
	# set name equal to the element of ranks in position self.rank
	# if self.suit is 'd', append suits[0] to name
	# elif self.suit is 'c', append suits[1] to name
	# elif self.suit is 'h', append suits[2] to name
	# else, append suits[3] to mane
	# return name
		ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
					"Nine", "Ten", "Jack", "Queen", "King"]
		suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
		name = ranks[self.rank - 1] + " of "
		if self.suit == "d":
			name += suits[0]
		elif self.suit == "c":
			name += suits[1]
		elif self.suit == "h":
			name += suits[2]
		else:
			name += suits[3]
		return name


def main():
	n = eval(input("Enter the number of cards to be generated: "))

	print()
	for i in range(n):
		rank = randrange(1, 14)
		suit = ["d", "c", "h", "s"][randrange(0, 4)]
		card = Card(rank, suit)
		print("The", card, "has a Blackjack value of", card.BJValue())

main()



