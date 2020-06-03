#02_test_binary_search.py

# Of course, you can't find mistakes during runtime if you don't run it.
# It's going to be very tedious manually running the whole program.
# Besides, sometimes you want to test specific, internal functions,
# which you can't directly access from the user interface.
# That's why Python has the unittest module.

from binary_search import find, UnorderedException

from unittest import main, TestCase

class BinarySearchTest(TestCase):
	def test_in_order(self):
		"A test method, which must start with test_"
		# You can have many test vectors.
		# Each one contains at least the input that you
		# feed to your function, or whatever code you want to test.
		# You can group a lot of them together,
		# if you're testing the same feature.
		# Here we have two test vectors,
		# inside one test method, which must start with "test_"
		in_order = [([1, 2, 3, 4], 3), ([-4, 3, 6, 19], 2)]
		# It's always a good idea to have a different technique
		# for testing the result, rather than recalculating
		# the same answer with the same technique.
		# Sometimes, that means manually creating the answers,
		# and include it in the test vector,
		# but other times, you can have simpler, but slower ways,
		# of getting the same results.
		# Or it's easier to check the result than to create it.
		for collection, target in in_order:
			index = find(collection, target)
			if (index >= 0):
				# For example, with finding,
				# you can check if the element is there.
				# For testing, you'll use "assert*"
				# methods of the class a lot.
				# They check if a condition is met.
				# For most variations, like here,
				# they check if a boolean or relationship
				# is True.
				self.assertEqual(target, collection[index])
			else:
				# Or if it really can't be found
				self.assertNotIn(target, collection)
				
	def test_bad_order(self):
		# You can also test if your code reports errors correctly,
		# by using assertRaises.
		out_of_order = [([1, 3, 2, 4], 3), ([19, -4, 3, 6], 2)]
		for collection, target in out_of_order:
			with self.assertRaises(UnorderedException):
				index = find(collection, target)

if (__name__ == "__main__"):
	# You can run unittest.main, to run the test in the script.
	# Or you can run the unittest module with the name of this module.
	main()
