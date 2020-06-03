# You can also bunch together different kinds of exceptions.

running = True

while (running):
	try:
		# First get the input.
		input_str = input("Please enter a number: ")
		input_value = float(input_str)
		print("1 / %f = %f", input_value, 1.0 / input_value)
	except (ValueError, ZeroDivisionError):
		# You just put the different types together, in parentheses.
		print("%s is not a valid input"%(input_str))
	except KeyboardInterrupt:
		# Not really an error, but want to stop.
		print("Stopping")
		running = False
