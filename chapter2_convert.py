# A program to convert Celsius temps to Fahrenheit 
# by: Susan Computewell
# introduction by Dora Belme

def main():
	# Introduction
	print("""
		Convert.py is designed to convert temperature in Celsius to temperatures
		in Fahrenheit. When prompted please enter the numerical value of the Celsius\
		temperature and we will provide the corresponding value in Fahrenheit.""")
	
	# The code
	celsius = eval (input ("What is the Celsius temperature? ") ) 
	fahrenheit = 9/5 * celsius + 32
	print ("The temperature is", fahrenheit, "degrees Fahrenheit.") 


main ()

input("Press the <Enter> key to quit.")