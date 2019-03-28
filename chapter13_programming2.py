class FibCounter:

	def __init__(self):
		self.__count = 0

	def getCount(self):
		return self.__count

	def fib(self, n):
		self.__count += 1
		if n < 3:
			return 1
		else:
			return self.fib(n-1) + self.fib(n-2)

	def resetCount(self):
		self.__count = 0

# create FibCounter object: ctr
# get n
# run ctr.fib method with argument n
# get count from ctr: count
# display information for user

ctr = FibCounter()
n = eval(input("Which Fibonacci number should we calculate? "))
ctr.fib(n)
count = ctr.getCount()
ctr.resetCount()
print('Number of times fib() is called when calculating fib(' + str(n) + ') is', count)

