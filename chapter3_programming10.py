# Program calculates the area of a triangle
# Input 3 sides

import math

def main():
	# Title of the Program
	print("Ladder Length Calculator\n")

	# Obtain the height and angle of the ladder from the user
	height = float(input("How high must the ladder reach (in feet)? "))
	degrees = float(input("What angle do you expect the ladder sit at" + \
		"(in degrees)? "))
	

	# Calculate the area
	angle_rad = degrees * math.pi / 180
	length = height / math.sin(angle_rad)


	# Display result for the user
	print("\nThe minimum length your ladder should be is", round(length,2), "feet.")


main()
