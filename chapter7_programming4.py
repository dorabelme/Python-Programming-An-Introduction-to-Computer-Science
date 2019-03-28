def main():
	credit = int(input("Enter your total credits accrued: "))

	if credit < 7:
		year = "Freshman"
	elif credit < 16:
		year = "Sophomore"
	elif credit < 26:
		year = "Junior"
	else:
		year = "Senior"
	print("You are classified as a", year + ".")
	
main()
