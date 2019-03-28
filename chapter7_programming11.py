def main():
	print("\nLeap Year Calculator")
	year = int(input("Enter a year in the common era >> "))
	
	is_leap = False

	if year % 4 == 0:
		if year % 100 != 0 or year % 400 == 0:
			is_leap = True

	if is_leap:
		print(year, "is a leap year.")
	else:
		print(year, "is not a leap year.")

main()


