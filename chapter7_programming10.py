def main():
	print("\nEaster Calculator")
	year = int(input("Enter a year between 1900 and 2099 >> "))
	
	while year < 1900 or year > 2099:
		print("Invalid year.")
		year = int(input("Enter a year between 1900 and 2099 >> "))

	a = year % 19
	b = year % 4
	c = year % 7
	d = (19 * a + 24) % 30
	e = (2 * b + 4 * c + 6 * d + 5) % 7

	day = 22 + d + e

	if year == 1954 or year == 1981 or year == 2049 or year == 2076:
		day -= 7
		
	if day > 31:
		print("Easter falls on April", day - 31, "in the year", str(year) +".")
	else:
		print("Easter falls on March", day, "in the year", str(year) +".")

main()