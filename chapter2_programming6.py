def main():
	print("This program calculates the future value of a n-year investment.")

	principal = eval(input("Enter the initial principal: "))
	apr = eval(input("Enter the annual interest rate: "))
	years = eval(input("Enter the number of year: "))

	for i in range(years):
		principal = principal * (1 + apr)

	print("The value in", years, "years is:", principal)


main()

