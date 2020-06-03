# Exceptions are used to remind you to clean things up.
# Some objects can also be cleaned up with "with".
# The most common us case is files.

# So with opens the file, and when you exit the block, it's closed.
# More generally, with lets you create an object, and assign it to a variable.

with open("with_file", "w") as outf:
	print("Write and close", file = outf)
