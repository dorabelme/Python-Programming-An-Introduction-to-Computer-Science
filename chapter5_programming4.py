def main():

	# Get a string of words from the user
	user_str = input("Please type in a phrase: ")

	# Split the user's string up at the space characters
	word_list = user_str.split()

	# Create an accumulator string named acronym. Then iterate through each word
	# in word_list and tack on the uppercase version of the first letter
	acronym = ""
	for word in word_list:
		acronym += word[0].upper()

	# Display the result for the user
	print("\nAn acronym for that phrase is", acronym + ".")

main()

