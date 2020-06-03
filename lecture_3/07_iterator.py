# I've mentioned iterators before.
# But what if you want to write your own iterator?
# How do you know when to stop? What would you return?

# Let's create a simple, custom version of range.
# It must always go from 0 to a positive number.
# Now we can define and raise exceptions by ourselves.

# The iterator should be a separate object,
# so you can use different iterators of the same collection.
class SimpleRangeIterator:
	# the current counter
	__current = 0
	# the upper limit
	__end = None
	def __init__(self, end):
		self.__end = end
	def __next__(self):
		"The method used for iteration"
		# Fetch the current value to return
		current = self.__current
		# Calculate the next value
		self.__current += 1
		# Only return a value if the iterator is still in range.
		if (self.__current <= self.__end):
			return current
		else:
			# Otherwise, raise the exception for stopping
			raise StopIteration

# We also need an exception if the upper limit is impossible.
class BadEndError(Exception):
	__end = None
	def __init__(self, end):
		self.__end = end
	def __str__(self):
		"We really just want to send a message"
		return "Upper limit must be positive, " + \
		       "but got %d"%(self.__end)

class SimpleRange:
	# the end of the range
	__end = None
	def __init__(self, end):
		if (end <= 0):
			# Raise an error exception
			raise BadEndError(end)
		self.__end = end
	def __iter__(self):
		return SimpleRangeIterator(self.__end)

# Let's give it a try
for i in SimpleRange(5):
	print(i)

input()
# Let's try something bad
SimpleRange(-1)
