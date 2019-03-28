def Ei_igh():
	return "Ee-igh, Ee-igh, Oh!"

def macD(animal, sound):
	print("Old MacDonald had a farm"  + Ei_igh())
	print("And on that farm he had a", animal + Ei_igh())
	print("With a", sound + ",", sound, "here and a", sound + ",", sound, "there")
	print("Here a", sound + ", there a", sound + ", everywhere a", sound + ",", sound + ".")
	print("Old MacDonald had a farm" + Ei_igh())


def main():
	macD('cow', 'moo')
	print()
	macD('pig', 'oink')
	print()
	macD('turkey', 'gobble')
	print()
	macD('snake', 'hiss')
	print()
	macD('antelope', 'snort')

main()




