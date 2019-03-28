principal = 1000
interest = eval(input("Enter the annual interest as decimal number " +
						"(ie 0.5 for 50%): "))

balance = principal
year = 0
while balance < 2 * principal:
	balance = balance * (1 + interest)
	year += 1

print("The time it will take for your investment to double in value at that " +
		"interest rate is", year, "years.")


