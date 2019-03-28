# Calculates the cost of an order

def main():
	COST_PER_POUND = 10.50
	SHIPPING_PER_POUND = 0.86
	SHIPPING_OVERHEAD = 1.5

	# Obtain the number of pounds shipped from the user
	pounds = int(input("Enter the number of pounds you wish to purchase: "))

	# Calculations
	subtotal = pounds * COST_PER_POUND
	shipping = SHIPPING_OVERHEAD + pounds * SHIPPING_PER_POUND
	total = subtotal + shipping

	# Display the result for the user
	print("\nThe order will cost $", round(total, 2), " in total.", sep='')


main()




