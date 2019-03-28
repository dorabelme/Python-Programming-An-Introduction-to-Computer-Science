# Program calculating the cost per square inch of a circular pizza
# Input is diameter and price

import math

def areaPizza(diameter):
	radius = diameter / 2			# need radius for our calculations, not diameter
	area = math.pi * radius ** 2
	return area

def cost(diameter, price):
	return price / areaPizza(diameter)


def main():
	# obtain the diameter and price from the user
	diameter = int(input("Enter the diameter of the pizza in inches: "))
	price = float(input("Enter the price of the pizza: "))

	# Display the result for the user with the cost rounded to 2 decimal places
	print("The cost is $", round(cost(diameter, price), 2), " per square inch.", sep='')


main()

