# So if you remembered the things I taught you last time,
# then theoretically, you can create any kind of program.
# In reality, that's not very convenient,
# and your program still doesn't know how to interact with the outside world.

# I mentioned in the introduction that Python uses several paradigms.
# That means that you have many options for organizing your code in an easy way.
# The first homework hopefully wasn't too long,
# but once you start coding real programs,
# the program will be doing a lot of work.
# Fortunately, you don't have to repeat code too much.
# You've already seen how you can reuse code. Where?
# But what if you want to reuse the code in different places?
# A lot of it might be a variation of the same thing,
# just in a different place, with some different properties.
# Each paradigms lets you vary a different property.
# If just a few pieces of data are different,
# you can use functions.
# Functions look a lot like math functions.
# You have a name, and some parameters, or functions inside parentheses,
# and they do something different based on those arguments.
# Where have you seen function calls before?
# Now we get to define our own.

# function with single parameter
# The name is inside the parentheses, as if you're declaring a variable.
def basic_function(name):
	print("Hello %s!"%(name))

# function with multiple parameters
# This time, you have multiple names, separated by a comma.
def double_argument(name, value):
	print("%s = %s"%(name, value))

# So you call a custom function like you call a regular function.
# The argument values are inside the parentheses.
basic_function("World")
double_argument("Yes", True)
