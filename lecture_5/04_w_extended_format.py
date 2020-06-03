# Is any of this useful? Just ask whoever designed string formatting.
# At the very least, it's very convenient.
# Last lecture, I showed how logging uses formatting with dictionaries.
# The format method kind of lets you do the same thing.

# Just look at the documentation.
print(str.format.__doc__)

# If you remember the first lecture, when I showed you the format method,
# When I had extra curly braces, there was an error.
# Do you remember what that error was? What exactly was causing that?
# So this is how formatting works with unordered arguments.
print("{key_1} {key_0}".format(key_0 = 0, key_1 = 1))

# And of course, we can combine ordered and unordered.
# Let's shake things up a bit.
# One ordered argument comes first, and the other comes last.
print("{} {key_1} {key_0} {}".format(-1, -2, key_0 = 0, key_1 = 1))

# What if we put a number in one of those curly braces?
# Can we have a number as a keyword?
print("{1} {key_1} {key_0} {0}".format(-1, -2, key_0 = 0, key_1 = 1))
# So we can repeat any argument, over and over.
print("{1} {key_1} {key_0} {0} {0} {0}".format(-1, -2, key_0 = 0, key_1 = 1))
#-2, 1 , 0, -1 , -1, -1
