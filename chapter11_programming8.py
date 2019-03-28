def removeDuplicates(lst):
	newList = []
	for elem in lst:
		if elem not in newList:
			newList.append(elem)
	lst [:] = newList

myList = [1,1,2,4,3,4,3,4,5,5,6,7,8,9,10,1]
removeDuplicates(myList)
print(myList)

