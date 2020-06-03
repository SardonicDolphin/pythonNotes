# Pretty nifty, right?
# But is this good for anything besides syntactic sugar?
# What if you want to wrap a function --any function?
# Remember that Python lets you pass arbitrary functions to other functions.
# You might not always know what the arguments are.

# Let's make a simple one.
# It takes any function, and logs its parameters.
def wrapper(wrappee, *ordered, **unordered):
	# Get the values of the arguments, as they would look in code
	# We want to see how the argument values look in code.
	args = list(map(repr, ordered))
	# The names will be directly turned into identifiers.
	args += list(map(lambda pair: "%s = %s" % (pair[0], repr(pair[1])),
			 unordered.items()))
	args_str = ", ".join(args)
	# Let's log its return value
	return_value = wrappee(*ordered, **unordered)
	# We can even get the name
	name = wrappee.__name__

	print("%s(%s) -> %s" % (name, args_str, return_value))

# Let's try it out on a simple math function
from math import sqrt
wrapper(sqrt, 225)

# Let's try something more complicated.
# int can take only one argument
input()
wrapper(int, "123")
input()
# But it also has an optional base.
# Let's try it without the name.
wrapper(int, "123", 10)
# And now with the name.
input()
wrapper(int, "123", base = 10)

# That looks convenient. So now what if you want to keep the wrapped function?
# No problem. Just make such a function.
def wrapped_int(*ordered, **unordered):
	return wrapper(int, *ordered, **unordered)

input("With a permanently wrapped function")
wrapped_int("123", base = 10)

# But you don't just want to wrap int.
# You want to wrap other functions, too,
# and you don't want to write a new function for it every time,
# no matter how small.
# If there was only a way to repeat the same calculation
# on different objects,
# and those objects could be functions, and you could output functions.
# What does that sound like?
def gen_wrapped_function(func):
	# You can do some pre-processing before creating the wrapped function.
	print("We will be wrapping function %s" % (func.__name__))
	def wrapped_function(*ordered, **unordered):
		return wrapper(func, *ordered, **unordered)
	return wrapped_function

# Let's use this a few more times.
wrapped_int_2 = gen_wrapped_function(int)
wrapped_sqrt = gen_wrapped_function(sqrt)

input("With generated wrapped function")
wrapped_int_2("123", base = 10)
wrapped_sqrt(225)

# OK. Looks like a really nice wrapper.
# Let's keep it. Then we can just overwrite the variables for the functions.
int = wrapped_int_2
sqrt = wrapped_sqrt

input("With redefined functions")
int("123", base = 10)
sqrt(225)

# Of course, you could have redefined it from the start.
# And if you define the wrapped function,
# Python has special syntax for that.

# Let's look back at gen_wrapped_function.
# That is what is called a decorator.
# If you've taken 1007, you learned about the decorator pattern.
# This is a generalized implementation of it.
# It takes a function as a parameter,
# and returns a function that has similar behavior.

# Say we want to have a wrapped add function.
# What the decorator does is this:
def adder(a, b):
	return a + b
adder = gen_wrapped_function(adder)

input("Our own, wrapped function")
adder(1, 2)

# Not bad. But Python has syntactic sugar for that too.
# You just add the at sign, and the expression for the function.
@gen_wrapped_function
def multiplier(a, b): # Let's try another function
	return a * b
input("Use decorator in annotation")
multiplier(2, 5)

input()
# One issue here, though, is that the actual name changes
# to the wrapped version.
print("Decorated function is now called: %s" % (multiplier.__name__))

# Now I said that the thing that comes after the "@" is an expression.
# It does not have to be exactly a function that processes another function,
# it just has to act like one.
# It could be a call to a function that returns a function...
# that returns a function.
# Let's say we want decorators that only show the first couple of
# ordered arguments.
def gen_decorator(n_args):
	# Now we can do even more preprocessing.
	print("Decorator generator is called for up to %d arguments" % (n_args))
	def decorator(to_wrap):
		def wrapped(*args, **kwargs):
			# Only cut off args if there are too many
			if (len(args) <= n_args):
				cut_args = args
			else:
				cut_args = args[ : n_args]
			print("First %d arguments: %s" %
			      (n_args, ", ".join(map(repr, cut_args))))
			return to_wrap(*args, **kwargs)
		return wrapped
	return decorator

input()
# Let's try it out on a function that sums all of its arguments.
# Notice that the expression is actually executed,
# which is why we have it print the number of arguments it will show.
@gen_decorator(3)
def summer(*args):
	return sum(args)

summer(1, 2, 3, 4, 5, 6)

input()
# Now try a similar decorator, but stricter,
# and for a function that multiplies all of its arguments.
@gen_decorator(2)
def producer(*args):
	product = 1
	for arg in args:
		product *= arg
	return product

producer(1, 2, 3)

# We could go on forever with this nesting.
