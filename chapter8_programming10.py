def main():
	print("Fuel Efficiency Calculator")
	infile = open("trip.txt", "r")

	miles_list = []
	gas_list = []
	odom1 = eval(infile.readline())
	for line in infile:
		odom2, gas = line.split()
		odom2 = eval(odom2)
		gas = eval(gas)
		mile = odom2 - odom1
		miles_list.append(mile)
		gas_list.append(gas)
		odom1 = odom2

	infile.close()

	print("\nLeg 		MPG")
	for i in range(len(miles_list)):
		mpg = miles_list[i] / gas_list[i]
		print("{0:2d} {1:13.1f}".format(i + 1, mpg))
	total_miles = sum(miles_list)
	total_gas = sum(gas_list)
	print("Total MPG: {0:5.1f}".format(total_miles / total_gas))

main()

