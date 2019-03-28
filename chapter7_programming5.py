def main():
	print("Body Mass Index Calculator")
	weight = eval(input("Enter your weight in pounds: "))
	height = eval(input("Enter your height in inches: "))

	BMI = weight * 720 / height ** 2

	if BMI < 19:
		print("\nYour BMI is a bit low.")
	elif BMI <= 26:
		print("\nYour BMI is considered healthy.")

	else:
		print("'nYour BMI is a bit high.")

main()

