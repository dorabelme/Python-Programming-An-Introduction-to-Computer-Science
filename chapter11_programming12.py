def censor(word):
	# Iterate through characters and replace all letters with an asterisk
	# This means that a censored word with a comma with still have the comma.

	for i in range(len(word)):
		if word[i].isalpha():
			word = word[:i] + '*' + word[i+1:]
	return word


def main():
	filename = input("Enter the name of the file to censor: ")
	text = open(filename, 'r')
	words_filename = input("Enter the name of the file containing the censored words")
	censored = open(words_filename, 'r')

	censored_words = censored.read().split()

	censored_text = ''
	for line in text:
		words = line.split()
		# Check if the letters in one of the 'words' in the line spells out
		# a censored word. If so, replace it with asterisk.
		for i in range(len(words)):
			word = '' 
			for letter in words[i]:
				if letter.isalpha():
					word += letter
			if word in censored_words:
				words[i] = censor(words[i])
	censored_text += ''.join(words) + '\n'

	text.close()
	censored.close()

	new_file = open('censored ' + filename, 'w')
	new_file.write(censored_text)
	new_file.close()

main()

