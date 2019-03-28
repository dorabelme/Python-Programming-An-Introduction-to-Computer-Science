# Program using Newton's method to approximate square root

import math

def main():
	# Title and description of the Program
	print("\nSquare Root Approximator\n")
	print("This program calculates the approximation of the square root of " +\
			"a number using Newton's method.")

	# Obtain the number to take the square root of, the number of times to improve
	# the 'guess', and the initial guess itself
	num = int(input("\nEnter the number whose square root you'd like to calculate: "))
	n = int(input("Enter the number of times Newton's method should iterate: "))
	guess = float(input("Enter your initial guess of what the square root should be: "))


	# Calculate the square root using Newton's method

	for i in range(n):
		guess = (guess + num / guess) / 2
		
	# Display result for the user
	print("\nThe approximate square root of ", num, " is ", guess, ".", sep="")
	print("\nThe error in this approximation is ", math.sqrt(num) - guess, ".", sep="")


main()




