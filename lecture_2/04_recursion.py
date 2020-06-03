# As with other languages, Python functions can perform recursion.
# What does that mean? It means that functions can be recursive.
# What's a recursive function? It's a function that performs recursion.
# It can call itself, but it had better stop somewhere.

# The most famous example is the Fibonacci sequence.
# The ith number is the sum of the last two numbers,
# and the first two are 0 and 1.
# It's an alterative way of doing loops.
def fib(i):
	# Base cases
	if (i < 0):
		return None
	elif (i == 0):
		return 0
	elif (i == 1):
		return 1
	else:
		# Recursive cases
		return fib(i - 1) + fib(i - 2)

for i in range(10):
	print(fib(i))

input()
# But usually, you don't want to use it where you can use a for or while loop.
# The way that function calls work make recursion more expensive.
# What's wrong with this?
def bad_recursion(i):
	if (i + i == 2 * i):
		return bad_recursion(i - 1)
	else:
		return False

bad_recursion(5)
