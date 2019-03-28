# Program calculates the distance to a lightning strike based on the time
# elapsed between the flash and the sound of thunder


def main():
	# Constants
	SPEED_OF_SOUND = 1100
	MILE_IN_FEET = 5280

	# Obtain the time elapsed from the user
	time = int(input("Enter the time that elapsed between the flash" + \
						"and the sound of thunder: "))

	# Calculations
	distance = SPEED_OF_SOUND * time 
	miles = distance // MILE_IN_FEET
	feet = distance % MILE_IN_FEET

	# Display the result for the user
	print("\nThe distance to the lightning strike is about", miles, "miles and", \
			feet, "feet from your current location.")


main()


