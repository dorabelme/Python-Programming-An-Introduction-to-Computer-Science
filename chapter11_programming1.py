from math import *

def getNumbers():
	nums = []			# start with an empty list

	# sentinel loop to get numbers
	xStr = input("Enter a number (<Enter> to quit) >> ")
	while xStr != "":
		x = float(xStr)
		nums.append(x)		# add this value to the list
		xStr = input("Enter a number (<Enter> to quit) >> ")
	return nums

def mean(nums):
	sum = 0.0
	for num in nums:
		sum = sum + num
	return sum / len(nums)

def stdDev(nums, xbar):
	return meanStdDev(nums)[1]

def meanStdDev(nums):
	# calculate mean
	sum = 0.0
	for num in nums:
		sum = sum + num
	xbar = sum / len(nums)

	# use mean to calculate std dev
	sumDevSq = 0.0
	for num in nums:
		dev = num - xbar
		sumDevSq = sumDevSq + dev * dev
	return xbar, sqrt(sumDevSq/len(nums)-1)


def median(nums):
	# sort the numbers into ascending order
	# if size of data is odd:
		# med = the middle value
	# else:
		# med = the average of the two middle values
	# return med

	nums.sort()
	size = len(nums)
	midPos = size // 2
	if size % 2 == 0:
		med = (nums[midPos] + nums[midPos - 1]) / 2
	else:
		med = nums[midPos]
	return med

def main():
	print("This program computes mean, median, and standard deviation.")


	data = getNumbers()
	xbar = mean(data)
	std = stdDev(data, xbar)
	med = median(data)

	print("\nThe mean is", xbar)
	print("The standard deviation is", std)
	print("The median is", med)

main()