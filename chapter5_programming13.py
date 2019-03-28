# File: chaos_modified.py
# A simple program illustrating chaotic behavior.
def main():

	print("This program illustrates chaotic function")
	infile = open('input_numbers.txt', "r")
	outfile = open('output_tables.txt', "w")

	for line in infile:
		num1_str, num2_str = line.split()
		num1 = eval(num1_str)
		num2 = eval(num2_str)	
		print('{0} {1:^8}	 {2:^8}'.format('index', num1, num2), file = outfile)
		print('-' * 27, file=outfile)
		for i in range(1,11):
			num1 = 3.9 * num1 * (1 - num1)
			num2 = 3.9 * num2 * (1 - num2)
			print('\n{0:^5} {1:8.6f}	 {2:8.6f}'.format(i, num1, num2), file=outfile)

	infile.close()
	outfile.close()

	outfile = open('output_tables.txt', 'r')
	out_list = outfile.read().split('\n')

	print("\nLet's read a line from our output file.")
	user_num = eval(input("Enter a table number: "))

	print("\nHere's table number:", user_num, "from the output file:\n")
	for i in range(len(out_list)):
		if 12 * (user_num - 1) <= i and i < 12 * user_num:
			print(out_list[i])

	outfile.close()


main()
