# Program calculates the area of a triangle
# Input 3 sides

import math

def main():
	# Title of the Program
	print("Triangle Area Calculator\n")

	# Obtain the three side lengths from the user
	a = float(input("Enter the first side length: "))
	b = float(input("Enter the second side length: "))
	c = float(input("Enter the third side length: "))

	# Calculate the area
	s = (a + b + c) / 2
	area = math.sqrt(s * (s - a) * (s - b) * (s - c))

	# Display result for the user
	print("\nThe area of your triangle is ", round(area,2), ".", sep="")


main()

