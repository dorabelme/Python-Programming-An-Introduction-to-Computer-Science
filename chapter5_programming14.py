def main():

	# Get filename from use
	filename = input("Enter the filename: ")

	# Open file and read it into a string
	file = open(filename, "r")
	file_str = file.read()

	# Initialize count variables
	line_count = 0
	word_count = 0
	char_count = 0

	# Count the characters, words, and lines
	for ch in file_str:
		char_count += 1
		if ch.isspace():
			word_count +=1
		if ch == "\n":
			line_count += 1

	# Display the file information
	print("\nFile Information")
	print("Line Count:		", line_count)
	print("Word Count:		", word_count)
	print("Character Count:		", char_count)

	# Close the file
	file.close()

main()


