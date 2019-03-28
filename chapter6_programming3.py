import math

def sphereArea(radius):
	return 4 * math.pi * radius ** 2


def sphereVolume(radius):
	return (4 / 3) * math.pi * radius ** 3


def main():
	print("Sphere Calculator")
	rad = eval(input("Enter a radius: "))

	print("\n	Data")
	print("-" * 20)
	print("{0:13} {1:>6.1f}".format("Surface Area:", sphereArea(rad)))
	print("{0:13} {1:>6.1f}".format("Volume:", sphereVolume(rad)))

main()


	