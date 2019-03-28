def main():
	# Get a string from the user
	user_input = input("Enter a sentence:")

	# Split string into list of words
	word_list = user_input.split()

	# Remove the ending punctuation mark from the last word
	word_list[-1] = word_list[-1][0:-1]

	# Count the number of words in the list and the number of letters total
	word_count = 0
	letter_count = 0

	for word in word_list:
		word_count += 1
		letter_count += len(word)

	# Calculate the average word length	
	average = letter_count / word_count

	# Display the number of words on screen
	print("The average word in your text has", average, "letters")

main()

