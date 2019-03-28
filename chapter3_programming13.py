# Program calculates the sum of a series of numbers

def main():
	# Title of the Program
	print("Sum of Arbitrary List Calculator\n")
	print("This program calculates the sum of a list of numbers.")

	# Obtain the number of numbers from the user
	n = int(input("\nEnter the number of numbers to be summed: "))

	# Calculate the sum
	total = 0

	for i in range(1, n + 1):
		number = float(input("Enter the number: "))
		total += number 
		
	
	# Display result for the user
	print("\nThe sum of your numbers is ", total, ".", sep="")


main()

