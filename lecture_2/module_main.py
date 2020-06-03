# You can have a script part in the module,
# which only runs if the __name__ variable is "__main__".

def module_function(x):
	"This function does nothing, until it is called"
	return x + 1

# The "__name__" variable is the module name,
# if the file is imported as a module.
# If the file is run directly, it is "__main__"
MODULE_MAIN_NAME = __name__

if (__name__ == "__main__"):
	print("module_function returned %d"%(module_function(1)))
