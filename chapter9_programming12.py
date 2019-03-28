# get number of steps, steps
# get number of simulations, n
# create an empty list to hold results of each sim, final_distances
# loop n times
	# initialize position to 0
	# loop steps times
		# randomly add or substract 1 from position
	# append the absolute value of position to final_distances
# calculate average distance, avg_distance
# print avg_distance

from random import randrange

def main():
	steps = eval(input("Enter the number of steps to take: "))
	n = eval(input("Enter the number of times to run the simulation: "))

	final_distances = []
	for i in range(n):
		position = 0
		for j in range(steps):
			one_step = randrange(2)
			if one_step == 0:
				position += 1
			else:
				position -= 1
		final_distances.append(abs(position))

	avg_distance = sum(final_distances) / len(final_distances)
	print("Average Final Distance: {0}".format(avg_distance))

main()

