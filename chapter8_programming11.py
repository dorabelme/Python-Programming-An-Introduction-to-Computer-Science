def main():
	print("Degree-Days Calculator")

	day = 1
	cool_days = 0
	heat_days = 0
	done = False
	while not done:
		temp = input("Enter the average daily temperature for day " +
						str(day) + " or quit to tabulate data: ")
		if temp.lower() != "quit" and temp.lower() !="q":
				temp = eval(temp)
				if temp > 80:
					cool_days += temp - 80
				elif temp < 60:
					heat_days += 60 - temp
				day += 1
		else:
			done = True 

		print("\nData")
		print("Number of heating degree-days: ", heat_days)
		print("Number of cooling degree-days: ", cool_days)

main()
