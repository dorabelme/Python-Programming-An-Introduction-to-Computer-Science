def fib(n):
	print('Computing fb(' + str(n) + ')')

	if n < 3:
		print('Leaving fib(' + str(n) + ') returning 1')
		return 1
	else:
		value = fib(n-1) + fib(n-2)
		print('Leaving fib(' + str(n) + ') returning', value)
		return value

print('fib(10) is', fib(10))


