def main():
	num1 = eval(input("Enter a number between 0 and 1: "))
	num2 = eval(input("Enter another number between 0 and 1: "))
	print("input              ", num1, "                              ", num2)
	print("------------------------------------------------------------------")
	for i in range(10):
		num1 = 3.9 * num1 * (1 - num1)
		num2 = 3.9 * num2 * (1 - num2)
		print("               ", num1, "                       ", num2)

main()

