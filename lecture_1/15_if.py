# Conditional statements

# The conditions depend on outside input
input_str = input("Please enter a number: ")

# You don't need to put parentheses around the conditions.
# Check if the input is an integer.
if input_str.isdigit() or (input_str[0] == "-" and input_str[1 : ].isdigit()):
	# Convert the string to an integer.
	# If you don't check, you'll get an error.
	input_int = int(input_str)
	if input_int == 0:
		print("That's nothing.")
	elif input_int < 0:
		# Full else if
		print("Don't be such a downer!")
	else:
		# Regular else
		print("Are you sure?")
else:
	# Regular else
	print("%s is not an integer"%input_str)
