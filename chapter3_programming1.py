# This program calculates the volume and surface areaa of a sphere
# Radius is given as input
# Written by Dora Belme

import math

def main():
	r = int(input("Enter the radius of the sphere: "))
	V = (4 / 3) * math.pi * (r ** 3)
	A = 4 * math.pi * (r ** 2)

	print("The volume of the sphere with", r, "radius is:", V)
	print("The surface area of the sphere with", r, "radius is", A)


main()