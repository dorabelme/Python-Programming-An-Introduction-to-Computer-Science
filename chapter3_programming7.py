# This program calculates the distance between two points

import math

def main():
	# Title of the program
	print("Distance Calculator")

	#Obtain the coordinates of the 2 points from the user
	print("To enter the coordinates of the point (x1, y1) you will need to " +\
		"type the coordinates without the parantheses seperated by a comma. " +\
		"Example: to input the coordinates of the point (2,3), you would " +\
		"just type 2, 3.")
	x1, y1 = eval(input("\nEnter the coordinates of the first point: "))
	
	x2, y2 = eval(input("\nEnter the coordinates of the second point: "))

	# Calculate the distance
	distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

	# Display the result for the user
	print("The distance between the points is: ", distance, ".", sep='')

main()
