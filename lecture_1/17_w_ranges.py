# Before we move on to for loops,
# Here's another iterable object that's very useful.
# Ranges
# In Python 3, ranges are a special class of immutable, sorted containers.
# kind of like automatically-generated tuples.
# The full input is three numbers.
# The starting number, which is included, the ending number, which is not,
# and the step, which can be positive or negative.
r = range(10, 30, 2)
r
# What are the numbers?
list(r)
# You can access it like a tuple
r[1]
r[9]

# The iterator'll stop before it's at or beyond the second number,
# Like here, where it can never reach 31,
# so it stops right before going past it.
list(range(10, 31, 2))
# It can also go backwards
list(range(30, 10, -2))
# See how it stops before reaching 10
# If the iterator can never go beyond the second number,
# the collection will be empty.
list(range(10, 31, -2))

# If you just give it two numbers, it'll assume the third number is 1
list(range(10, 20))

# If you give it just one number, it'll assume that the first number is 0
list(range(10))

# In Python 2, ranges are functions that return lists.
# So they are mutable.
range(10)
