def main():
	# Get a string from the user
	user_input = input("Enter a sentence:")

	# Split string into list of words
	sentence = user_input.split()

	# Count the number of words in the list
	count = 0
	for word in sentence:
		count += 1

	# Display the number of words on screen
	print("There are", count, "number of words in your text.")

main()


