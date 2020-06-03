# Now to help you keep things even more organized,
# you can comment the function.
# Just put a string after the header.

# They can be a short line.
def small_commented():
	"This function has only one line of comments"
	return None

# Or a long block string.
def big_commented(required, optional = 1):
	"""commented(required[, optional]) = required * optional

This function has a lot of documentation,
so it needed multiple lines."""

	return required * optional

# If you use strings, instead of the sharp sign,
# the comments also are an attribute of the function,
# called __doc__
# Yes. Functions are objects, too.

print(small_commented.__doc__)
print()
print(big_commented.__doc__)

# Most built-in functions also have documentation
