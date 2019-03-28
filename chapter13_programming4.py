def myMax(lst):
	# base case
	if len(lst) == 1:
		return lst[0]
	# other cases
	subMax = myMax(lst[1:])
	if lst[0] > subMax:
		return lst[0]
	else:
		return subMax

# Test run
myList = [1,-1,2,-2,5,15,-91]
print('The maximum of myList is', myMax(myList))

