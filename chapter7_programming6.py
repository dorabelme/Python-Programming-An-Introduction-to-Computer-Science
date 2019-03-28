def main():
	print("Speeding Violation Fine Calculator")
	limit = eval(input("Enter the speed limit: "))
	speed = eval(input("Enter your speed: "))

	if speed < limit:
		print("\nYour speed was legal.")
	elif speed > limit and speed < 90:
		fine = 50 + (speed - limit) * 5
		print("\nYour fine will be $" + str(fine) + ".")
	else:
		fine = 250 + (speed - limit) * 5
		print("\nYour fine will be $" + str(fine) + ".")

main()
