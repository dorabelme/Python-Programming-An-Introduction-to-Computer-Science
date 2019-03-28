# This program calculates the date of Easter


def main():
	# Title of the program
	print("Gregorian Epact Calculator")

	year = int(input("\nEnter a 4-digit calendar year: "))

	# Calculate the epact
	c = year // 100
	epact = (8 + c // 4 - c + (8 * c + 13) // 25 + 11 * (year % 19)) % 30
	
	# Display the result for the user
	print("\nThe Gregorian epact for the year ", year, " is ", epact, ".", sep='')

main()