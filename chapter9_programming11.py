# get number of rolls, n, from user
# initialize wins to 0
# loop n times
	# simulate a roll for each die
	# if all 5 dice are the same
			# add 1 to wins
# calculate probability as wins / n
# display probability

from random import randrange

def main():
	n = eval(input("Enter the number of times to roll 5 dice: "))

	wins = 0
	for i in range(n):
		d1 = randrange(1, 7)
		d2 = randrange(1, 7)
		d3 = randrange(1, 7)
		d4 = randrange(1, 7)
		d5 = randrange(1, 7)
		if d1 == d2 and d1 == d3 and d1 == d4 and d1 == d5:
			wins += 1
	prob = wins / n
	print("Estimated probability of a 5-of-a-Kind: {0:0.4%}".format(prob))

main()

