def main():
	# The index of each character in this string represents the score
	# associated with that letter grade. E.g. scores[4] = 'B' because a score
	# of 4 gives letter grade B.

	scores = "FFDCBA"

	# Get the quiz score
	quiz_score = eval(input("Enter the points scored on the quiz: "))

	# Display the letter grade
	print('\nThe grade for that score is ' + scores[quiz_score] + ".")

main()
