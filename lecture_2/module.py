# I've been reusing variables and functions in the same file.
# But if you write all the variables and functions in the same file,
# things can get messy really quickly.
# And what if you want to write programs in multiple modules?

"You can also comment modules with strings."

# The stuff inside a module is nothing new.

def module_function(x):
	"A function in a module"
	if (x == 0):
		return "You gave me nothing!"
	elif (x < 0):
		return "This is bad"
	else:
		return "This is good"

# A variable in a module
MODULE_VAR = 3.14

MODULE_VAR_2 = 2.72
