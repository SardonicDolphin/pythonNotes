# Today I'll be teaching you some advanced concepts
# that help make your code even more flexible.
# First I'll talk about more advanced things you can do with functions,
# and then I'll show you how you can use Python to run other programs
# on your computer.

# So far, all the functions I've shown you were pretty fixed
# in terms of input and output.
# Sure, you had some optional arguments,
# but even those had values, and there was still an upper bound.
# And the number of objects the function returns
# is fixed once it returns.

# Turns out, you don't even have to know all the argument names
# ahead of time.
# In Java and C, you might have seen functions with ... for arguments.
# Python has something very similar, but better.

# We have an arbitrary number of arguments,
# and we don't even give them names.
# All you need to do is put a single star in front of the argument name,
# which could really be anything.
def print_args(*ordered_args):
	print("Arguments: " + " ".join(map(str, ordered_args)))

# Let's print out all the arguments.
print_args(0, 1, 2, 3)
print_args(4, 5, 6)
print_args(7)

input()

# You've actually seen this before.
# Somewhere where you can have an arbitrary number of unnamed arguments.

# How does this work? What is the starred argument?
# Obviously it's ordered. So that gives us two types.
# Also, when you make the call, the arguments are fixed.
# Let's take a look.

def get_ordered_args_type(*mystery_type):
	print("Ordered arguments are of type %s" % (type(mystery_type)))

get_ordered_args_type(0, 1)

input()

# Now what's the deal with the star?
# Why did I take it away? What happens if I don't?
# We can see how it looks like if we pass the arguments
# to another function, with or without the stars
def try_star(*starred):
	def nested_callee(*arbitrary):
		print("\t%d arguments, starting from %s" % (len(arbitrary),
							    arbitrary))
	print("With star:")
	nested_callee(*starred)
	print("Without star:")
	nested_callee(starred)

try_star(0, 1, 2, 3)
