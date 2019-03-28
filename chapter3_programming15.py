# Program approximates the value of pi

import math

def main():
	# Title and description of the Program
	print("Pi Approximator\n")
	print("This program calculates the approximation of pi based on" +\
			"approximating on infinite sum by a finite one.")

	# Obtain the number of terms from the user
	n = int(input("\nEnter the number of terms of the finite sum: "))

	# Calculate the sum
	total = 0

	for i in range(n):
		total = total + 4 * (-1) ** i / (2 * i + 1)
		
	# Display result for the user
	print("\nThe approximate value of pi is ", total, ".", sep="")
	print("\nThe error in this approximation is ", math.pi - total, ".", sep="")


main()





