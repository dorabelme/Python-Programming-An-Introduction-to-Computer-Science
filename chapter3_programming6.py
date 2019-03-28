# This program calculates the slope of a line through two points

def main():
	# Title of the program
	print("Slope Calculator")

	#Pbtain the coordinates of the 2 points from the user
	print("To enter the coordinates of the point (x1, y1) you will need to " +\
		"type the coordinates without the parantheses seperated by a comma. " +\
		"Example: to input the coordinates of the point (2,3), you would " +\
		"just type 2, 3.")
	x1, y1 = eval(input("\nEnter the coordinates of the first point: "))
	
	x2, y2 = eval(input("\nEnter the coordinates of the second point: "))

	# Calculating the slope
	slope = (y2 - y1) / (x2 - x1)

	print("The slope of your line is: ", slope, ".", sep='')

main()

