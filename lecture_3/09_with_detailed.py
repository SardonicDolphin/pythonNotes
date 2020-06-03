# How does it all work in the background?
# It uses the method __enter__ and __exit__.
# Let's use a wrapper around the file object, to see what is happening.

class FileWrapper:
	__wrapped_file = None
	def __init__(self, path):
		self.__wrapped_file = open(path, "r")
		print("Created")
	def __enter__(self):
		"""The __enter__ method returns the object to be used
Note that it does not have to be itself.
"""
		print("Entered")
		return self.__wrapped_file
	def __exit__(self, exc_type, exc_value, traceback):
		self.__wrapped_file.close()
		print("Exited")

with FileWrapper("with_file") as fwf:
	print("Read: %s"%(fwf.read()))
