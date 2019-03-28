# Program calculates the average of a series of numbers entered


def main():
	# Title of the Program
	print("Average of Arbitrary List Calculator\n")
	print("This program calculates the average of a list of numbers.")

	# Obtain the number of numbers from the user
	n = int(input("\nEnter the number of numbers to be averaged: "))

	# Calculate the sum
	total = 0

	for i in range(1, n + 1):
		number = float(input("Enter the number: "))
		total += number 
		average = total / n
		
	
	# Display result for the user
	print("\nThe sum of your numbers is ", average, ".", sep="")


main()

