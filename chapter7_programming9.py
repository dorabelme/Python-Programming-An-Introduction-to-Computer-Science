def main():
	print("\nEaster Calculator")
	year = int(input("Enter a year between 1982 and 2048 >> "))
	
	while year < 1982 or year > 2048:
		print("Invalid year.")
		year = int(input("Enter a year between 1982 and 2048 >> "))

	a = year % 19
	b = year % 4
	c = year % 7
	d = (19 * a + 24) % 30
	e = (2 * b + 4 * c + 6 * d + 5) % 7

	day = 22 + d + e

	if day > 31:
		print("Easter falls on April", day - 31, "in the year", str(year) +".")
	else:
		print("Easter falls on March", day, "in the year", str(year) +".")

main()


# get year
# while year is not between 1982 and 2048, get year again
# set a, b, c, d, e, and date to values from book
# if date > 31
	# display date April  + (date - 31)
# else
	# display March + date
