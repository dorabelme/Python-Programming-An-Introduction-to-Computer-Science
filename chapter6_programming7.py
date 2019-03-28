# Program computes the nth Fibonacci number

def nth_Fib(n):
	if n == 1 or n == 2:
		return 1
	else: 
		return nth_Fib(n-1) + nth_Fib(n-2)



def main():
	# Title and description of the Program
	print("Fibonacci Calculator\n")
	print("This program calculates the nth Fibonacci number.")

	# Obtain the number of terms from the user
	usr_int = int(input("\nEnter an integer n: "))
		
	# Display result for the user
	print("\nThe Fibonacci number F(",usr_int,") is ", nth_Fib(usr_int), ".", sep="")
	

main()
