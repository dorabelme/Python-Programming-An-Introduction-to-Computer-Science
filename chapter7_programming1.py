def main():
	print("Wage Calculator")
	hours = float(input("Enter your hours worked: "))
	rate = float(input("Enter your hourly pay: "))

	if hours > 40:
		wage = 40 * rate + (hours - 40) * 1.5 * rate
		print("With your overtime, you made ${0:0.2f}".format(wage))
	else:
		wage = hours * rate
		print("You made ${0:0.2f}".format(wage))

main()


