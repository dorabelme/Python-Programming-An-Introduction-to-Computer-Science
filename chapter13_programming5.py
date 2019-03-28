# function: baseConversion
# input: num, base

# if 0 <= num < base:
	# convert num to a string
	# return that string
# else:
	# convert num % base to string: str1
	# return baseConversion(num//base, base) + str1

def baseConversion(num, base):
	# Base case
	if 0 <= num < base:
		return str(num)
	# Recursice cases
	else:
		return baseConversion(num//base, base) + ' ' + str(num % base)


def main():
	invalid = True
	while invalid:
		try:
			num = int(input('Enter a nonnegative integer: '))
			if num < 0:
				print('Invalid input,\n')
			else:
				base = int(input('Enter a base (an integer greater than 1): '))
				if 2 <= base:
					invalid = False
				else:
					print('Invalid input.\n')
		except:
			print('Invalid input.\n')
	print(num, 'in base', base, 'is', baseConversion(num, base))

main()

