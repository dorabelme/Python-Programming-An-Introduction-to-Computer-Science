def main():

	# The Latin alphabet. The index of each letter is one less than the
	# numeric value of that letter.
	alphabet = "abcdefghijklmnopqrstuvwxyz"

	# Get name from user
	full_name = input("Enter a full name: ")
	name_list = full_name.split()

	# Add up the values of each letter of the name
	name_value = 0
	for name in name_list:
		for ch in name:
			name_value += alphabet.find(ch.lower()) + 1

	# Display the numeric value of the name on the screen
	print("The numeric value of", full_name, "is", str(name_value) + ".")

main()
