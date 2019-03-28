# File: chaos_modified.py
# A simple program illustrating chaotic behavior.
def main():

	print("This program illustrates chaotic function")
	num1 = eval(input("Enter a number between 0 and 1: "))
	num2 = eval(input("Enter a number between 0 and 1: "))

	# Display table
	print('\n{0} {1:^8} {2:^8}'.format('index', num1, num2))
	print('-' * 27)

	for i in range(1,11):
		num1 = 3.9 * num1 * (1 - num1)
		num2 = 3.9 * num2 * (1 - num2)
		print('\n{0:^5} {1:8.6f} {2:8.6f}'.format(i, num1, num2))

main()



