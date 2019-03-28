# input: myList
# create an empty test to hold shuffled numbers: newList
# while myList is not empty
	# randomly select a number from 1 to len(myList)-1 : ind
	# add myList[ind] to newList
	# remove myList[ind] from myList
# set the values of myList to those of newList

from random import randrange

def shuffle(myList):
	newList = []
	while len(myList) > 0:
		ind = randrange(len(myList))
		newList.append(myList.pop(ind))
	myList[:] = newList