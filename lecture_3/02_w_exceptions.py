# Now to some actual, unexpected behavior.
# The first, and most standard kind of unexpected behavior is exceptions.
# Exceptions are generally used when something goes wrong, but not always.
# You might have seen them already when there is bug in your program.

# For example, if you access a variable that does not exist
print(bad_variable)
print(NameError.__doc__)

# Or if you try to turn a non-integer string into an integer.
int("not an integer")
print(ValueError.__doc__)
# You've seen isint before. Why might this be better?

# Or you try to access an index that is too high
[1, 2][5]
print(IndexError.__doc__)

# Or a dictionary key that does not exist
{}["key"]
print(KeyError.__doc__)

# You could read a file that does not exist.
open("bad_file", "r")
print(FileNotFoundError.__doc__)

# And division by zero also creates an error
1 / 0
print(ZeroDivisionError.__doc__)
