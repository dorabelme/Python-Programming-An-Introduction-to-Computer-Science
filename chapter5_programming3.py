def main():

	# The index of each character in this string represents the score
	# associated with that letter grade.
	scores = "F" * 60 + "D" * 10 + "C" * 10 + "B" * 10 + "A" * 11

	# Get the exam score
	exam_score = eval(input("Enter the points scored on the exam: "))

	# Display the letter grade
	print("\nThe grade for that score is ", scores[exam_score] + ".")

main()

