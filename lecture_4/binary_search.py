#binary_search.py

# The search function only expects ordered inputs,
# so it throws an exception otherwise.
class UnorderedException(Exception):
	__index = None
	__first = None
	__second = None
	def __init__(self, index, first, second):
		self.__index = index
		self.__first = first
		self.__second = second
	def __str__(self):
		return "Out of order at %d: %s should come after %s"% \
		       (self.__index, self.__first, self.__second)

def check_order(indexed_collection):
	for index in range(len(indexed_collection) - 1):
		first = indexed_collection[index]
		second = indexed_collection[index + 1]
		if (first > second):
			raise UnorderedException(index, first, second)

def _find(ordered_collection, target, start, end):
	"The actual search routine, assuming the collection is ordered"
	if (not end):
		end = len(ordered_collection)

	if (start == end):
		return -1

	middle = (start + end) // 2

	middle_element = ordered_collection[middle]

	if (target == middle_element):
		return middle
	elif (target < middle_element):
		return _find(ordered_collection, target, start, middle)
	else:
		return _find(ordered_collection, target, middle + 1, end)

def find(indexed_collection, target):
	"The main search routine, which we want to test"
	check_order(indexed_collection)
	n_elements = len(indexed_collection)
	if (target == indexed_collection[0]):
		return 0
	if ((n_elements > 0) and (target == indexed_collection[-1])):
		return n_elements - 1
	return _find(indexed_collection, target, 0, n_elements)
