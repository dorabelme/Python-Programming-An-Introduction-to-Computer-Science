# Python Calculator
# by: Dora Belme

def main():
	print("Welcome to the Python Calculator!")

	for i in range(100):
		expression = eval(input("Enter a valid mathematical expression or the program " +\
					"will crash badly: "))
		print("Result: ", expression)

main()

