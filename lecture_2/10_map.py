# One of the most common uses of functional programming is
# in the map function.
# It takes a function that takes a single input, and a collection.

print(map.__doc__)

def wait():
	"""Just a trick to wait for user to press enter before continuing
for both Python 2 and 3"""
	try:
		input()
	except:
		raw_input()

def to_map(x):
	"The function we will use in map"
	print("Calling to_map(%s)" % (x))
	return 2 * x

def print_map_result(map_result):
	"A helper function for printing the results of map multiple times."
	strings = map(str, map_result)
	# Say we want to separate the parts with something that is not
	# a newline.
	# You could use a loop, and then remember that
	# you don't have a separator before the first element,
	# or after the last one.
	print(", ".join(strings))

xs = range(10)
map_result = map(to_map, xs)

print("Called map")
# By the way, what's missing here?
wait()

print("First run. Always works.")
print_map_result(map_result)
# What happens in Python 3?
wait()
print("Second run")
print_map_result(map_result)

wait()
# If you want to keep the same return value, even after running it once,
# make a copy of it.
print("Making a copy first, this time")
constant_map_result = tuple(map(to_map, xs))
# Notice that this time we already iterated over everything.

print("First run with copy. Always works.")
print_map_result(constant_map_result)
print("Second run with copy. Always works.")
print_map_result(constant_map_result)
