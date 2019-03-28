def grade(score):
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else:
		return "F"


def main():
	# Get the exam score
	score = eval(input("Enter the points scored on the exam: "))

	while score < 0 or score > 100:
		print("Invalid input.")
		score = eval(input("Enter the exam score: "))

	letter_grade = grade(score)
	# Display the letter grade
	print("\nThe letter grade for that exam score is ", letter_grade + ".")

main()

