# You can also tell Python which module to run as a script,
# using the -m option, and the module name.

def module_2_function(x):
	"This funtion does nothing, until it is called"
	return x * 2

if (__name__ == "__main__"):
	print("module_2_function returned %d"%(module_2_function(2)))
