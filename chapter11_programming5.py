def count(myList, x):
	count = 0
	for elem in myList:
		if x == elem:
			count += 1
	return count

def isin(myList, x):
	is_in = False
	for elem in myList:
		if x == elem:
			is_in = True
			break
	return is_in

def index(myList, x):
	for i in range(len(myList)):
		if myList[i] == x:
			return i
	return None

def reverse(myList):
	return myList[-1::-1]


def sort(myList):
	sorted = False
	while not sorted:
		sorted = True
		for i in range(1, len(myList)):
			if myList[i-1] > myList[i]:
				myList[i-1], myList[i] = myList[i], myList[i-1]
				sorted = False