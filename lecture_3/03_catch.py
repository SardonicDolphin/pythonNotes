# If we just left the exceptions like that,
# your program will stop before you want to.
# And sometimes, you want to allow some of these exceptions,
# You know in Java, you have to handle them.
# You can also do it in Python, but it's optional here.

# Let's say you want to keep asking the user for a number,
# and then output its reciprocal. What can go wrong?

while (True):
	# First get the input.
	input_str = input("Please enter a number: ")

	# If you're doing something, where you expect an error,
	# you put it in a "try" block
	try:
		# This time, we want a float, not an int.
		input_value = float(input_str)
	except ValueError:
		# Then you put an "except" block,
		# that says what error you expect.
		# The ValueError exception here is optional.
		# If you take it away,
		# this block will handle every exception.
		# But that's not usually a good idea,
		# because if I make a mistake,
		# for example I use a bad variable,
		# I would not know about it.
		# Here, we only want to catch that the string is invalid,
		# and try again.
		print("%s is not a valid number"%(input_str))
		continue

	# Now on to the calculation
	try:
		print("1 / %f = %f", input_value, 1.0 / input_value)
	except ZeroDivisionError:
		print("Don't have a reciprocal of 0")
	finally:
		# And for all cases, you can add the finally block.
		# You usually use this when you have to do some cleaning up.
		print("Tried to find the reciprocal of %f" % (input_value))

# And we press Ctrl-C to exit.
# That is also an exception.
