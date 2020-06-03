# We can pass in functions as parameters,
# which, unlike in the previous example,
# are not always known ahead of time.
# The solver functions are not so interesting,
# except that they can take in any functions.
# The interesting part comes after the function declarations.

def is_negative(value):
	"""A helper function for normalizing the sign of a number to a boolean.
That lets us use boolean operations for comparing signs."""
	return value < 0;

def binary_solver(start, end, to_solve, error):
	"""Solve a function using the intermediate value theorem.
start: the start of the interval
end: the end of the interval
to_solve: the function for which we want to find the zero.
	Assumed to be continuous.
error: the return value can be at most this far away from the real solution"""
	# The middle value, which will be used for recursion.
	middle = (start + end) / 2
	# The middle value is close enough.
	if (abs(end - start) <= error):
		return middle

	# Find the y values of the beginning and end.
	start_y = to_solve(start)
	end_y = to_solve(end)

	# Check if the solution hasn't already been found.
	if (start_y == 0):
		return start
	if (end_y == 0):
		return end
	middle_y = to_solve(middle)
	if (middle_y == 0):
		return middle

	# The function has to cross y = 0 somewhere
	# in the interval,
	# which is ensured if the y values
	# at the ends of the interval
	# have opposite signs.
	start_negative = is_negative(start_y)
	middle_negative = is_negative(middle_y)
	end_negative = is_negative(end_y)

	# Can't guarantee a solution if both ends have the same sign.
	# If they have the opposite sign,
	# we can pick the new interval,
	# to ensure that the ends have opposite y-values.
	if (start_negative == end_negative):
		return None
	elif (start_negative ^ middle_negative):
		return binary_solver(start, middle, to_solve, error)
	else:
		return binary_solver(middle, end, to_solve, error)

def linear(x):
	"A linear function we want to solve."
	return 4 * x - 3

def quadratic(x):
	"A quadratic function we want to solve."
	return x ** 2 - 1

# The error tolerance
ERROR = 10 ** -32

# We can use the same solver function
# to solve different functions.
linear_solution = binary_solver(-10, 10, linear, ERROR)
print("linear(%f) ~ %f"%(linear_solution, linear(linear_solution)))
quadratic_solution = binary_solver(0, 10, quadratic, ERROR)
print("quadratic(%f) ~ %f"%(quadratic_solution, quadratic(quadratic_solution)))
