# Program using Newton's method to approximate square root

import math

def nextGuess(guess, x):
		return (guess + x / guess) / 2

def main():
	# Title and description of the Program
	print("\nSquare Root Approximator\n")
	print("This program calculates the approximation of the square root of " +\
			"a number using Newton's method.")

	# Obtain the number to take the square root of, the number of times to improve
	# the 'guess', and the initial guess itself
	num = int(input("\nEnter the number whose square root you'd like to calculate: "))
	times = int(input("Enter the number of times Newton's method should iterate: "))
	
	sq_root = num / 2 
	for i in range(times):
		sq_root = nextGuess(sq_root, num)

	error = abs(math.sqrt(num) - sq_root)

	# Display result for the user
	print("\n{0:26} {1}".format("Result of Newton's method:", sq_root))
	print("\n{0:26} {1}".format("Error:", error))


main()




