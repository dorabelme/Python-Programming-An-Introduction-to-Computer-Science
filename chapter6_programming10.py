def acronym(phrase):
	# Split the user's string up at the space characters
	word_list = phrase.split()

	# Create an accumulator string named acronym. Then iterate through each word
	# in word_list and tack on the uppercase version of the first letter
	acr = ""
	for word in word_list:
		acr += word[0].upper()
	return acr

def main():

	# Get a string of words from the user
	phrase = input("Please type in a phrase: ")

	# Display the result for the user
	print("\nAn acronym for", phrase + " phrase is", acronym(phrase)+ ".")

main()

