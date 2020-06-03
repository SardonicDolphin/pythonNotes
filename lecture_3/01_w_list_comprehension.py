# I want to start off by extending an idea that we saw last time,
# namely the map function, and introduce something more flexible.
# For the rest of the lecture,
# I'll be talking about some rather unintuitive aspects of Python,
# and how to deal with them.
# But first, I'll extend on some things I talked about last time.
# Last class, I showed you some extra power of functional programming.
# But it is not always necessary.
# I've been showing you examples of using map.
# But sometimes you don't want to use it.
# First, you might have something very simple that needs no function,
# lambda or otherwise.
# Also, map keeps all of the same elements,
# but what if you want to filter some of them out?
# That's where list comprehension comes in.

# Let's say you have this list of strings
strings = "This is a list of strings".split(" ")

# You want to turn it all into upper case.
# How do you do it in map?
# What if you couldn't use map, and only used for loops.
# Neither one looks good. But list comprehensions get the best of both worlds.

# With list comprehensions, you don't need a function.
[string.upper() for string in strings]
# Think of this like a for loop, squashed into square brackets,
# except the loop body is an expression that gives a value,
# and it's in front.
# It's like this
new_list = []
for string in strings:
	new_list.append(string.upper())

# Just to round out or comparison with map, who thinks this will print
# in Python 3?
[print(string) for string in strings]

# You can even nest the for loop.
# This is something that map cannot do, even if you already have the function.
# Say we also have a list of numbers.
numbers = [24, 23, 9234]
[(string, number) for string in strings for number in numbers]

# Actually, it can be any collection. Like a tuple
numbers = (24, 23, 9234)
[(string, number) for string in strings for number in numbers]
# The things you loop over don't have to be distinct.
# Again, the same rules as for loops,
# except you have to have an expression in the loop body.
# You could loop over the strings, and then the characters in each string
[c.upper() for string in strings for c in string]
# Or loop twice over the same thing, to get all the pairs
[(s0, s1) for s0 in strings for s1 in strings]

# And as I promised, I can filter things out.
# Say I only want the first letter of non-empty strings.
strings3 = "Some  strings will be empty".split(" ")
strings3

# Just put an if at the end.
print([string[0] for string in strings3 if len(string) > 0])
# Now, what happened first?
# The operation at the beginning or the filter at the end?
