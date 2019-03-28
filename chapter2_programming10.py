# A program to convert kilometers to miles 
# by: Susan Computewell

KM_TO_MI = 0.62
def main():
	km = eval (input ("What is the distance in kilometers? ") ) 
	mi = km * KM_TO_MI
	print ("The distance is", mi, "miles.") 


main ()