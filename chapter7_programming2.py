def main():
	score = int(input("What is your quiz score? "))

	if score >= 0 and score < 6:

		if score == 5:
			print("A")
		elif score == 4:
			print("B")
		elif score == 3:
			print("C")
		elif score == 2:
			print("D")
		else:
			print("Your grade is F.")
	else:
		print("That is not a valid score.")

main()

