# Everything I mentioned before is similar to function pointers in C or C++.
# But what gives Python the functional flavor is that
# you can also create custom functions on the fly,
# by having functions return functions.

def generate_linear(slope, intercept):
	"""generate_linear(slope, intercept) -> linear function"""
	# Define a function inside another function,
	# much like you would define normal function.
	# Why is this useful? Why can't I just define a function normally,
	# outside of this function?
	def linear(x):
		"An automatically-generated linear function"
		return slope * x + intercept
	return linear

# Generate two linear functions
linear_0 = generate_linear(1, 0)
linear_1 = generate_linear(0, 1)

print("linear_0:\n%s"%(linear_0.__doc__))
print("linear_1:\n%s"%(linear_1.__doc__))

# Run them both
for x in range(10):
	print("%d: %d %d"%(x, linear_0(x), linear_1(x)))
