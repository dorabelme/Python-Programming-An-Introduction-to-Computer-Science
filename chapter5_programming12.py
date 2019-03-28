# A program to compute the value of an investment
# Carried 10 years into the future

def main():
	print("This program calculates the future value of a 10-year investment.")

	principal = eval(input("Enter the amount of investment: "))
	apr = eval(input("Enter the annual interest rate: "))

	# Display table
	print('\n{0} {1:^8}'.format('Year', 'Value'))
	print('-' * 16)

	for i in range(11):
		print('{0:>3} ${1:7.2f}'.format(i, principal))
		principal = principal * (1 + apr)

main()

