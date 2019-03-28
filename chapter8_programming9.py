def main():
	print("Fuel Efficiency Calculator")
	odom1 = eval(input("Please enter the starting odometer reading: "))

	miles_list = []
	gas_list = []
	usr_in = input("Enter the odometer reading and gas used seperated by a " +
					"space: ")
	while usr_in != "":
		odom2, gas = usr_in.split()
		odom2, gas = eval(odom2), eval(gas)
		miles_list.append(odom2 - odom1)
		gas_list.append(gas)
		odom1 = odom2
		usr_in = input("Enter the odometer reading and gas used seperated by a " +
					"space: ")


	print("\nLeg 		MPG")
	for i in range(len(miles_list)):
		mpg = miles_list[i] / gas_list[i]
		print("{0:2d} {1:13.1f}".format(i + 1, mpg))
	total_miles = sum(miles_list)
	total_gas = sum(gas_list)
	print("Total MPG: {0:5.1f}".format(total_miles / total_gas))

main()

