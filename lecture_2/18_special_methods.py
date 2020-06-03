# The nice thing about Python classes
# is that you can override simple operations.
# You can do something like that in C++, too,
# but there, you also have to worry about pointers and memory.

# Let's try something simple.
# Like a finite sequence. A sequence is just an ordered set of numbers.
# It's like a list. But we want some different functionalities.
# For example, if you add two sequences,
# we don't concatenate them, but add the respective elements.

class FiniteSequence:
	"""A finite sequence of numbers.
Additions between sequences are done per element."""
	# We use a list in the backend, which implements a lot for us.
	__elements = None
	def __init__(self, elements):
		"""FiniteSequence(elements):
elements: collection of elements"""
		# Make a copy, to be safe.
		self.__elements = list(elements)
	def __setitem__(self, key, value):
		"self[key] = value"
		self.__elements[key] = value
	def __getitem__(self, key):
		"read operation: self[key]"
		return self.__elements[key]
	def __len__(self):
		"Defines what len(self) does"
		return len(self.__elements)
	def __iter__(self):
		"Defines how iterator works, for example in for loop"
		return self.__elements.__iter__()
	def __add__(self, other):
		"""Add the respective elements of the sequences.
If a sequence does not have an element, treat it as 0"""
		combo_list = []
		index = 0
		# Note that we are already using the redefined operators
		while (index < len(self) or index < len(other)):
			if (index >= len(self)):
				new_element = other[index]
			elif (index >= len(other)):
				new_element = self[index]
			else:
				new_element = self[index] + other[index]
			combo_list.append(new_element)
			index += 1
		# You should return a new object,
		# instead of changing the old one.
		# This makes intuitive sense.
		# Say you add 1 and 2. You get 3,
		# but 1 and 2 are still the same number.
		return FiniteSequence(combo_list)
	def __str__(self):
		return str(self.__elements)

seq_0 = FiniteSequence([1, 2, 3])
seq_1 = FiniteSequence([-0.5, -1, -1.5, -2, -2.5, -3])
# Let's use some of the special methods
# Print the sequence.
print("Before: %s"%(seq_0))
# Get the first element
print("First element: %d"%(seq_0[0]))
# Change the first element
seq_0[0] = 100
print("After: %s"%(seq_0))

# The length:
print("seq_0 has %d elements:"%(len(seq_0)))
# Iterate through the elements:
for element in seq_0:
	print("\t%d"%(element))

print("%s + %s = %s"%(seq_0, seq_1, seq_0 + seq_1))

# There are many more operators.
# Not all of them make sense all the time,
# but you can use them to make life easier.
# You can find most of them in the list and integer type.
input()
def get_specials(obj):
	"""helper function for getting special methods,
which start and end with double underscores."""
	return [name for name in dir(obj) if name.startswith("__") and
					     name.endswith("__")]
print(set(get_specials(list)).union(set(get_specials(int))))
# you can delete items. You can compare objects.
# You can do more math and logic operations.
