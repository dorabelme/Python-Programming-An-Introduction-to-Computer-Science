def lyrics(num, activity):
	print("The ants go marching", num, "by", str(num) + ", hurrah, hurrah!")
	print("The ants go marching", num, "by", str(num) + ", hurrah, hurrah!")
	print("The ants go marching", num, "by", str(num) + ",")
	print("The little one stops to", activity + ",")
	print("And they all go marching down...")
	print("In the ground...")
	print("To get out...")
	print("Of the rain.")
	print("Boom!" * 3)

def main():
	numbers = ["one", "two", "three", "four", "five", "six", "seven", \
				"eight", "nine", "ten"]
	activities = ["activity 1",
					"activity 2",
					"activity 3",
					"activity 4",
					"activity 5",
					"activity 6",
					"activity 7",
					"activity 8",
					"activity 9",
					"activity 10"]

	for i in range(10):
		lyrics(numbers[i], activities[i])

main()



