def squareEach(nums):
	for i in range(len(nums)):
		nums[i] = nums[i] * nums[i]

def sumList(nums):
	total = 0
	for num in nums:
		total += num
	return total

def toNumbers(strList):
	for i in range(len(strList)):
		strList[i] = eval(strList[i])


def main():
	filename = input("Enter the filename: ")
	infile = open(filename, "r")
	lines = infile.readlines()

	for i in range(len(lines)):
		lines[i] = lines[i].split()
		toNumbers(lines[i])
		squareEach(lines[i])
		print(sumList(lines[i]))

	infile.close()

main()

