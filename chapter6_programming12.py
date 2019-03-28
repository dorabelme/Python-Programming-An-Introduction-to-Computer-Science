def sumList(nums):
	total = 0
	for num in nums:
		total += num
	return total

def main():
	# Testing
	list_of_lists = [[], [2], [1,2,4,10], [-1,-6,1,6], [1.1,2.2]]
	for lst in list_of_lists:
		print(sumList(lst))

main()

