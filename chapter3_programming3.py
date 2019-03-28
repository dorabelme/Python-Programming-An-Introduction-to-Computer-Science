# The program computes the molecular weight of a carbohydrate in grams per mole

def main():
	# The constanta

	H_WEIGHT = 1.00794		# grams / mole
	C_WEIGHT = 12.0107
	O_WEIGHT = 15.9994

	#Obtain the number of each element in the molecule from the user
	hydrogen = int(input("Enter the number of H atoms in the hydrocarbon: "))
	carbon = int(input("Enter the number of C atoms in the hydrocarbon: "))
	oxygen = int(input("Enter the number of O atoms in the hydrocarbon: "))

	# Calculations
	total_H_weight = hydrogen * H_WEIGHT
	total_C_weight = carbon * C_WEIGHT
	total_O_weight = oxygen * O_WEIGHT
	total_weight = total_H_weight + total_C_weight + total_O_weight

	# Display the result for the user
	print("The molecular weight of your hydrocarbon is", round(total_weight, 4), \
		"grams per mole.")

main()

