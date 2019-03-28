def main():
	print("Degree-Days Calculator")
	temp_file = open("temps.txt", "r")

	cool_days = 0
	heat_days = 0
	for temp in temp_file:
		temp = eval(temp)
		if temp > 80:
			cool_days += temp - 80
		elif temp < 60:
			heat_days += 60 - temp
	
	temp_file.close()

	print("Number of heating degree-days: ", heat_days)
	print("Number of cooling degree-days: ", cool_days)

main()
