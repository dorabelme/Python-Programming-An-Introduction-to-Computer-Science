from math import sqrt

def main():
	print("Prime Finder")
	num = eval(input("Enter a positive integer: "))

	is_prime = True
	for i in range(2, round(sqrt(num) + 1)):
		if num % i == 0:
			is_prime = False
			break
	if is_prime:
		print(num, "is a prime number.")
	else:
		print(num, "is not a prime number")

main()

