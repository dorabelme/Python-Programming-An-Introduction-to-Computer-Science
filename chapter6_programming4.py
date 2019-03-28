def sumN(n):
	total = 0
	for i in range(1, n+1):
		total += i
	return total 

def sumNCubes(n):
	total = 0
	for i in range(1, n+1):
		total += i ** 3
	return total


def main():
	print("Sum Calculator")
	n = eval(input("Enter a number: "))

	print("\nThe sum of the first", n, "natural numbers is", str(sumN(n))+".")
	print("\nThe sum of the cubes of the first", n, "natural numbers is", str(sumNCubes(n))+".")
	
main()


	