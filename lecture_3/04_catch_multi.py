# Actually, you can be more fine grained about handling errors.
# For one thing,
# you can handle multiple kinds of exceptions from the same try block.
# We can do that with the last example.

# Since it's all in one place, we can also see how to use KeyboardInterrupt

running = True

while (running):
	try:
		# First get the input.
		input_str = input("Please enter a number: ")
		input_value = float(input_str)
		print("1 / %f = %f", input_value, 1.0 / input_value)
	except ValueError:
		print("%s is not a valid number"%(input_str))
	except ZeroDivisionError:
		print("Don't have a reciprocal of 0")
	except KeyboardInterrupt:
		# Not really an error, but want to stop.
		print("Stopping")
		running = False
