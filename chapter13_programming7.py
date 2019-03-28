from time import time


def recC(n, k):
	# base cases
	if k == 0:
		return 1
	if k == 1:
		return n
	if n < k:
		return 0

	# recursive cases
	return recC(n-1, k-1) + recC(n-1, k)

def loopC(n, k):
	if k == 0:
		return 1
	if k == 1:
		return n
	if n < k:
		return 0
	Cnk = 1
	for i in range(k+1, n+1):
		Cnk *= i
	for i in range(1, n-k+1):
		Cnk //= i
	return Cnk

def main():
	n, k = eval(input("Enter n, k: "))

	# time recC
	start = time()
	binCoeff = recC(n, k)
	end = time()
	# print time for recC
	print('It took', end - start, 'seconds to compute that C(' + str(n) + ', '
			+ str(k) + ') = ', binCoeff, 'using recC.')

	# time loopC
	start = time()
	binCoeff = loopC(n, k)
	end = time()

	# print time for loopC
	print('It took', end-start, 'seconds to compute that C(' + str(n) + ','
			+ str(k) + ') =', binCoeff, 'sing loopC.')

main()


