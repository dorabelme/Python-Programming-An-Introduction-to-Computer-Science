def pal_checker(str1):
	# base cases
	if len(str1) < 2:
		return True

	# recursive cases
	# if first or last are not letter, remove that character and check again
	if not str1[0].isalpha():
		return pal_checker(str1[1:])
	if not str1[-1].isalpha():
		return pal_checker(str1[:-1])

	# otherwise, check the first against the last and run pal_checker on
	# everything in between
	if (str1[0].lower() == str1[-1].lower()) and pal_checker(str1[1:-1]):
		return True
	else:
		return False


def main():
	# ask the user for string and check if it's a palindrome
	user_str = input("Enter a string of characters: ")
	if pal_checker(user_str):
		print("That is a palindrome")
	else:
		print("That is not a palindrome")

main()

