def digitsToEnglish(num):
	digits = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
				'Eight', 'Nine']

	# Base case
	if 0 <= num < 10:
		return digits[num]

	# Recursive cases
	else:
		return digitsToEnglish(num//10) + " " + digits[num % 10]

def main():
	invalid = True
	while invalid:
		try:
			num = int(input('Enter a nonnegative integer: '))
			if num < 0:
				print('Invalid input,\n')
			else:
				invalid = False
				
		except:
			print('Invalid input.\n')
	print('The digits of', num, 'in English are', digitsToEnglish(num))

main()