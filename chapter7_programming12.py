def is_leap(year):
	leap = False

	if year % 4 == 0:
		if year % 100 != 0 or year % 400 == 0:
			leap = True
	return leap


def main():
	is_valid = True
	thirty_one_day_months = [1, 3, 5, 7, 8, 10, 12]
	print("\nValid Date Calculator")
	date = input("Enter a date in XX/XX/XXXX format >> ")
	
	# Check if it is in the correct format
	date_list = date.split("/")
	if len(date_list) != 3:
		is_valid = False
	else:
		month, day, year = date_list

		# Check if month, day, and year can be converted to ints
		try:
			month = int(month)
			day = int(day)
			year = int(year)

			# Check if values are in correct ranges
			if month > 12 or month < 1 or day > 31 or day < 1 or year < 1:
				is_valid = False
			elif month not in thirty_one_day_months and day == 31:
				is_valid = False

			# Factor in Februaries, taking into account leap years
			if is_leap(year) and month == 2 and day == 30:
				is_valid = False
			elif not is_leap(year) and month == 2 and day > 28:
				is_valid = False

		except:
			is_valid = False

	# If date passed all the tests, then it's valid. Otherwise, it is not
	if is_valid:
		print("That's a valid date.")
	else:
		print("That's not a valid date.")

main()


