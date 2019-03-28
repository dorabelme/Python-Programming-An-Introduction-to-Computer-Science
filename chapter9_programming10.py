from random import random

def main():
	printIntro()
	darts = getNumDarts()
	pi_est = simThrows(darts)
	printEst(pi_est)

def printIntro():
	print("Dart Estimate of Pi")

def getNumDarts():
	return eval(input("Enter the number of darts to be thrown: "))

def simThrows(darts):
	hits = 0
	for i in range(darts):
		if hitOneThrow():
			hits += 1
	pi_est = 4 * (hits / darts)
	return pi_est

def hitOneThrow():
	x = 2 * random() - 1
	y = 2 * random() - 1
	if x ** 2 + y ** 2 <= 1:
		return True 
	return False 
	
def printEst(pi_est):
	print("\nPi Estimate: {0:0.4f}".format(pi_est))

if __name__ == '__main__':
	main()


