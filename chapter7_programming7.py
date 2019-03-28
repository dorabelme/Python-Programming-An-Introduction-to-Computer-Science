def mil_time_to_decimal(time_str):
	hr_str, min_str = time_str.split(':')
	hr = int(hr_str)
	minute = int(min_str)
	return hr + minute / 60

def main():
	PRE_9_RATE = 2.5		# Dollars per hour
	POST_9_RATE = 1.75		# Dollars per hour

	print("Babysitting Bill Calculator")
	start_str = input("\nEnter the start time in 24-hour format: ")
	start = mil_time_to_decimal(start_str)
	end_str = input("Enter the return time in 24-hour format: ")
	end = mil_time_to_decimal(end_str)

	if end < 21:
		cost = (end - start) * PRE_9_RATE
	elif start < 21 and end >= 21:
		cost = (21 - start) * PRE_9_RATE + (end - 21) * POST_9_RATE
	else:
		cost = (end - start) * POST_9_RATE

	print("The total babysitting bill comes to ${0:0.2f}".format(cost))

	
main()


# get the starting time for the job in 24-hour format
# convert the starting time to a decimal number
# get the end time for the job in 24-hour format
# convert the end time to a decimal number

# if end number < 21
	# set cost equal to (end-start) * 2.50
# else if start < 21 and end >= 21
	# set cost equal to [(21-start) * 2.50 + (end-21) * 1.75]
# otherwise
	# set cost equal to (end-start) * 1.75
# display the cost on the screen

# Function input: string containing a time in 24-hour format
# Plit the string into a list of strings at the colon
# convert the first number in the list to an int and assign it to hr
# convert the second number in the list to an int and assign it to minute
# Function output: hr + minute / 60