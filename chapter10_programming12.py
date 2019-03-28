from random import randrange
from graphics import *

class Card:

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		self.imagefile = "Playing_Cards/" + self.__str__() + ".png"

	def getRank(self):
		return self.rank

	def getSuit(self):
		return self.suit

	def BJValue(self):
		if self.rank <= 10:
			return self.rank
		elif self.rank != "Joker":
			return 10
		else: 
			return 0


	def __str__(self):

	# set ranks equal to a list containing the names of each rank
	# set suits equal to al ist containing the names of each suit
	# set name equal to the element of ranks in position self.rank
	# if self.suit is 'd', append suits[0] to name
	# elif self.suit is 'c', append suits[1] to name
	# elif self.suit is 'h', append suits[2] to name
	# else, append suits[3] to mane
	# return name
		ranks = ["Joker", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
					"Nine", "Ten", "Jack", "Queen", "King"]
		suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
		name = ranks[self.rank]
		if self.suit == "d":
			if name != "Joker":
				name += "of" + suits[0]
			else:
				name = "Red" + name
		elif self.suit == "c":
			if name != "Joker":
				name += "of" + suits[1]
			else:
				name = "Black" + name
		elif self.suit == "h":
			if name != "Joker":
				name += "of" + suits[2]
			else:
				name = "Red" + name
		else:
			if name != "Joker":
				name += "of" + suits[3]
			else:
				name = "Black" + name
		return name

	def draw(self, win, center):
		Image(center, self.imagefile).draw(win)

def main():
	win = GraphWin("Poker Hand", 800, 400)
	win.setCoords(0, 0, 16, 2)
	win.setBackground("green")

	for i in range(5):
		rank = randrange(0, 14)
		suit = ["d", "c", "h", "s"][randrange(0, 4)]
		card = Card(rank, suit)
		card.draw(win, Point(2 + 3 * i, 1))

	win.getMouse()
	win.close()
	
main()



