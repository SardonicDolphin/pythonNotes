# But you've already seen that you don't have to return anything.
# In other functions, those are "void"-type functions.
# But what's missing here in the Python function definitions?

# This function never explicitly returns anything.
def never_return():
	print("Nothing to return")
	# It implicitly returns None

# This function explicitly returns None
def explicitly_return_none():
	return None

# This function returns an explicit value only sometimes
def sometimes_return(arg):
	if (hasattr(arg, "__add__")):
		# Return the doubled value
		return arg + arg
	# Is this legal?

print_return = print("Called print")
print("print returned %s"%(repr(print_return)))
input()
return_value = never_return()
print("never_return returned %s"%(repr(return_value)))
input()
return_value = explicitly_return_none()
print("explicitly_return_none returned %s"%(repr(return_value)))
input()
return_value = sometimes_return(1)
print("sometimes_return(1) returned %s"%(repr(return_value)))
# Here might be the only time we use is. For checking if something is None.
# There is only one none object.
if (return_value is not None):
	print("Returned a real value")
# None also happens to have a boolean value, False,
# but why don't you want to use that?
input()
# Now let's try the second case, where it returns nothing.
return_value = sometimes_return({})
print("sometimes_return({}) returned %s"%(repr(return_value)))
if (return_value is None):
	print("Returned None")
