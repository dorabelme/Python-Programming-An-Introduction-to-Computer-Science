def squareEach(nums):
	for i in range(len(nums)):
		nums[i] = nums[i] * nums[i]

def main():
	# Testing
	list_of_lists = [[], [2], [1,2,4,10], [-1,-6,1,6], [1.1,2.2]]
	for lst in list_of_lists:
		squareEach(lst)
		print(lst)

main()

