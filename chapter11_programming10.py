def main():
	# Get n
	n = eval(input("Enter an integer greater than one: "))

	# Create our list of numbers and a list to contain the primes
	num_list = list(range(2,n+1))
	prime_list = []

	while num_list != []:
		# Remove first number from num_list and add to prime_list
		first_num = num_list.pop(0)
		prime_list.append(first_num)

		# Remove multiples of that number
		for num in num_list:
			if num % first_num == 0:
				num_list.remove(num)

	# Print out the primes
	print("\nThe primes less than or equal to", n, "are")
	for i in range(len(prime_list)):
		print('{0:5d}'.format(prime_list[i]), end='')
		if i % 8 == 7:
			print()

	print()

main()

