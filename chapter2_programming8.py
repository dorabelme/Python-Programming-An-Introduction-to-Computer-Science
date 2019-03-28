def main():
	print("This program calculates the future value of a 10-year investment.")


	principal = eval(input("Enter the initial principal: "))
	rate = eval(input("Enter the annual interest rate: "))
	periods = eval(input("Enter the number of times the interest is compounded each year: "))
	years = eval(input("Enter the number of year: "))

	for i in range(10 * periods):
		principal = principal * (1 + rate / periods)

	print("The value in", years, "years is:", principal)


main()
