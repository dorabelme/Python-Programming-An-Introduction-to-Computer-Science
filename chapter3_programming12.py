# Program calculates the sum of the cubes of the first n natural numbers

def sum_cubes():
	# Title of the Program
	print("Sum of Cubes Calculator\n")

	# Obtain the n number from the user
	print("This program calculates the sum of the cubes of the first n integers.")
	n = int(input("Enter the number: "))
	

	# Calculate the sum
	total = 0
	for i in range(1, n + 1):
		total = total + i ** 3
	
	
	# Display result for the user
	print("\nThe sum of the cubes of the first ", n, " integers is ", total, ".", sep="")


sum_cubes()

