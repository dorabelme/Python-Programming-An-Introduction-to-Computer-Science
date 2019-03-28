# Converts day month and year numbers into two date formats

def main():
	# get the day month and year
	day, month, year = eval(input("Please enter day, month, and year " +\
									"numbers: "))

	date1 = "{1:02d}/{0:02d}/{2}".format(day, month, year)
	
	months = ["January", "February", "March", "April",
				"May", "June", "July", "August",
				"September", "October", "November", "December"]

	monthStr = months[month - 1]
	date2 = "{1} {0}, {2}".format(day, monthStr, year)

	# output result in month day, year format
	print("The date is", date1, "or", date2 + ".")


main()

