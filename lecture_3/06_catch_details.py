# But now we lost some information about the specific error.
# We can still print it, with the as keyword,
# which lets us assign the exception to a variable.

running = True

while (running):
	try:
		# First get the input.
		input_str = input("Please enter a number: ")
		input_value = float(input_str)
		print("1 / %f = %f", input_value, 1.0 / input_value)
	except (ValueError, ZeroDivisionError) as ex:
		# We can print out exactly what the error is.
		print("%s is not a valid input: %s"%(input_str, ex))
	except KeyboardInterrupt as ie:
		# We can also print the message for a single error
		# There actually is nothing to print, here
		print("Stopping: %s"%(ie))
		running = False
