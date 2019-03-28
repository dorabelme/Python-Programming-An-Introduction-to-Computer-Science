# Display title
print("\n" + " "*42 + "Windchill Factors")
# Display column titles
print("Wind" + " "*41 + "Temperature")
print("\033[4mSpeed", end="  ")
for T in range(-20,61,10):
	print(format(T, "10d"), end="")
print("\033[0m")

# Calculate and display wind speeds
for V in range(0,51,5):
	print(format(V, "^5d") + " "*4, end="")
	for T in range(-20,61,10):
		# If the windspeed is 0, then the windchill factor doesn't come into
		# effect ,yet
		if V == 0:
			print(format(T, "10.1f"), end="")
		# Otherwise, we apply the windchill formula
		else:
			windchill = 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275*T * (V ** 0.16)
			print(format(windchill, "10.1f"), end="")
	print()

print()