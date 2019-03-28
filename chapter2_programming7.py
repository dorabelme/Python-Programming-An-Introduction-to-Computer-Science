def main():
	print("This program calculates the future value of a n-year investment.")

	recur = eval(input("Enter the fixed amount deposited each year: "))
	apr = eval(input("Enter the annual interest rate: "))
	years = eval(input("Enter the number of year: "))

	
	principal = 0
	for i in range(years):
		# amount deposit at the beginning of the year
		principal += recur
		# interest added at the end of the year
		principal = principal * (1 + apr)


	print("The value in", years, "years is:", principal)


main()

