total = 0
for num in range(0, n+1):
	total += num

total = 0
for num in range(2*n):
	if num % 2 == 1:
		total += num

total = 0
user_num = eval(input("Enter a number, 999 to quit: "))
while user_num != 999:
	total += user_num
	user_num = eval(input("Enter a number, 999 to quit: "))

counter = 0
while n != 1:
	n = n // 2
	counter += 1