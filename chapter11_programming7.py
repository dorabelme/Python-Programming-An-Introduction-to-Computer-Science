def innerProd(x, y):
	sum = 0
	for (xi, yi) in zip(x, y):
		sum += xi * yi
	return sum


list1 = [1,2,94,4]
list2 = [2,-4,6,-13.2]

print(innerProd(list1, list2))
print(1 * 2 + 2 * -4 + 94 * 6 + 4 * -13.2)

