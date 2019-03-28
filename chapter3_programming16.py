# Program computes the nth Fibonacci number

def main():
	# Title and description of the Program
	print("Fibonacci Calculator\n")
	print("This program calculates the nth Fibonacci number.")


	# Obtain the number of terms from the user
	n = int(input("\nEnter an integer n: "))

	# First two Fibonacci numbers
	n1 = 1
	n2 = 1

	# Calculate the nth Fibonacci numbers from the 2 before
	for i in range(3, n + 1):
		n1, n2 = n2, n1 + n2
		
	# Display result for the user
	print("\nThe Fibonacci number F(",n,") is ", n2, ".", sep="")
	

main()
