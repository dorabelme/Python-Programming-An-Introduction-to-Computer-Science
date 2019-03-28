def main():
	score = int(input("What is your quiz score? "))

	if score >= 0 and score < 100:

		if score >= 90:
			grade = "A"
		elif score >= 80:
			grade = "B"
		elif score >= 70:
			grade = "C"
		elif score >= 60:
			grade = "D"
		else:
			grade = "F"
		print("Your grade is", grade + ".")
	else:
		print("That is not a valid score.")

main()
