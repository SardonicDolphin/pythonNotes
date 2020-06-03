# There is a way you can change values outside of the function
# by reassigning them.
# But as you've already seen in the last lecture,
# that doesn't happen automatically.

global_int = 0

def increment_global():
	# You first have to say that you want to use the global version
	global global_int
	global_int += 1

print("Before: %d"%(global_int))
increment_global()
print("After: %d"%(global_int))

input()

# In Python 3, but not Python 2, you can be more fine grained.
# Say you're in a nested function.
# You want to get the variables in the outside function,
# not the global scope.
# For example, here's a faster implementation of Fibonacci's sequence
def gen_fib():
	# The variables we want to access are in the function.
	a, b = 0, 1
	def fibber():
		# Say that we want to use the variables in the outer function
		nonlocal a, b
		old_a = a
		# Reassign, according to the sequence
		a, b = b, a + b
		return old_a

	return fibber

fibber = gen_fib()

for fib_i in range(10):
	print(fibber())

new_fibber = gen_fib()
for fib_i in range(10):
	print(new_fibber())
