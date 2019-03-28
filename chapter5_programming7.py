def main():

	# Get string and key from user
	user_str = input("Enter the text you'd like to encode: ")
	key = int(input("Enter an integer to act as the key value for the encryption "))

	# Encode the message
	enc_str = ""
	for ch in user_str:
		enc_str += chr(ord(ch) + key)

	# Display the encoded message
	print("\nYour encrypted message reads:")
	print(enc_str)

	# Decode the message
	dec_str = ""
	for ch in enc_str:
		dec_str += chr(ord(ch) - key)

	# Display the encoded message
	print("\nYour decrypted message reads:")
	print(dec_str)

main()

