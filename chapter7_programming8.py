def main():
	print("\nSenate and House Eligibility Calculator")
	age = int(input("\nEnter your age >> "))
	citizenship = int(input("Enter the number of years you've been a citizen >> "))

	if age >= 30 and citizenship >= 9:
		print("\nYou are eligible to run for the Senate of the House of Representatives.")
	elif age >= 25 and citizenship >= 7:
		print("\nYou are eligible to run for the House of Representatives but not the Senate.")
	else:
		print("\nSorry, you are not eligible to run for the Senate or the House of Representatives.")

main()
