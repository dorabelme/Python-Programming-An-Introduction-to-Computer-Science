def main():
	print("Euclid's algorithm")
	m = eval(input("Enter the first integer: "))
	n = eval(input("Enter the second integer: "))
	m_orig = m
	n_orig = n

	while m != 0:
		n , m = m, n % m
	
	print("The GCD of", m_orig, "and", n_orig, "is", str(n) + ".")
	

main()

