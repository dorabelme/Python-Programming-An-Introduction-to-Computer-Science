def contains_4_letters(word):
	count = 0
	for letter in word:
		if letter.isalpha():
			count += 1
	if count == 4:
		return True
	return False

def censor(word):
	for i in range(len(word)):
		if word[i].isalpha():
			word = word[:i] + '*' + word[i+1:]
	return word

# get filename from user: filename
# open file in read mode
# create empty string: censored_txt
# loop through each line in the file
	# split up the line into a list of words: words
	# loop through each word in words
		# if word containes exactly 4 letters
			# censor word
	# join words back into a string
	# concatenate censored_text with that string
# close the file
# open a new file in write mode
# write censored_text to the new file
# close the new file

def main():
	filename = input("Enter the file name: ")
	text = open(filename, 'r')

	censored_text = ''
	for line in text:
		words = line.split()
		for i in range(len(words)):
			if contains_4_letters(words[i]):
				words[i] = censor(words[i])
		censored_text += ''.join(words) + '\n'

	text.close()
	new_file = open('censored ' + filename, 'w')
	new_file.write(censored_text)

	new_file.close()

main()

