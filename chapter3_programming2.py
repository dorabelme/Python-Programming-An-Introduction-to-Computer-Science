# Program calculating the cost per square inch of a circular pizza
# Input is diameter and price

import math

def main():
	# obtain the diameter and price from the user
	diameter = int(input("Enter the diameter of the pizza in inches: "))
	cost = float(input("Enter the cost of the pizza: "))

	radius = diameter / 2			# need radius for our calculations, not diameter
	area = math.pi * radius ** 2
	cost_per_sqin = cost / area

	# Display the result for the user with the cost rounded to 2 decimal places
	print("The cost is $", round(cost_per_sqin, 2), " per square inch.", sep='')


main()

