from math import sqrt


def is_prime(num):
	is_prime = True
	for i in range(2, round(sqrt(num) + 1)):
		if num % i == 0:
			is_prime = False
			break
	return is_prime


def main():
	print("Prime Finder")
	num = eval(input("Enter a positive integer: "))

	print("The following are all of the prime numbers less than or equal to " +
			str(num) + ":")
	for i in range(2, num + 1):
		if is_prime(i):
			if i == 2:
				print(2, end='')
			else:
				print(",", i, end="")

	print()

main()

