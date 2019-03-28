from chapter10_programming12 import Card

def main():
	# open file
	infile = open("cardsFor13", 'r')

	# create list of card objects
	cardObjects = []
	for line in infile:
		items = line.split()
		rank = int(items[0])
		suit = items[1]
		card = Card(rank, suit)
		cardObjects.append(card)

	# sort list by rank
	cardObjects.sort(key=Card.getRank)

	# sort list by suit
	cardObjects.sort(key=Card.getSuit)

	# print out cards
	for card in cardObjects:
		print(card.__str__())

	# close file
	infile.close()

if __name__ == '__main__':
	main()

	