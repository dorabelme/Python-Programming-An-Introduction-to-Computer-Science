def main():
	print("Fibonacci Calculator")
	n = int(input("Enter a positive integer: "))

	prev = 1
	fib = 1 
	for i in range(2,n):
		temp = prev
		prev = fib
		fib = temp + fib
		
	print("The value of Fibonacci(" +str(n) +") is", fib)

main()