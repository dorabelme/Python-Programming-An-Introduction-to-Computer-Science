from math import sqrt
from random import randrange

def main():
	steps = eval(input("Enter the number of steps to take: "))
	n = eval(input("Enter the number of times to run the simulation: "))

	final_distances = []
	for i in range(n):
		x = 0
		y = 0
		for j in range(steps):
			one_step = randrange(4)
			if one_step == 0:
				x += 1
			elif one_step == 1:
				x -= 1
			elif one_step == 2:
				y += 1
			else:
				y -= 1
		distance = sqrt(x ** 2 + y ** 2)
		final_distances.append(abs(distance))

	avg_distance = sum(final_distances) / len(final_distances)
	print("Average Final Distance: {0:0.4f}".format(avg_distance))

main()

