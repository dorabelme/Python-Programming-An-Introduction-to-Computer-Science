def main():

	alphabet = "abcdefghijklmnopqrstuvwxyz"
	abcs = alphabet * 2 + alphabet.upper() * 2

	# Get string and key from user
	user_str = input("Enter the text you'd like to encode: ")
	key = int(input("Enter an integer between 1 and 25 to act as the key" +\
						"value for the encryption: "))

	# Encode the message
	enc_str = ""
	for word in user_str.split():
		for ch in word:
			enc_str += abcs[abcs.find(ch) + key]
		enc_str += " "
	enc_str = enc_str[:-1]


	# Display the encoded message
	print("\nYour encrypted message reads:")
	print(enc_str)

	# Decode the message
	dec_str = ""
	for word in enc_str.split():
		for ch in word:
			dec_str += abcs[abcs.find(ch) + 26 - key]
		dec_str += " "
	dec_str = dec_str[:-1]
		

	# Display the encoded message
	print("\nYour decrypted message reads:")
	print(dec_str)

main()



