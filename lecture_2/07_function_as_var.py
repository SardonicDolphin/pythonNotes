# And since functions are objects, they can also be assigned to variables,
# beside the name that you gave them.
# In fact, Python also supports functional programming.
# What does that mean? Aren't we already using functions?
# Well, yes. But C also uses functions, and it is not considered functional.
# Turns out you can not only vary data, but also parts of the computation.
# It's useful if you have a huge process,
# but in the middle, you can plug in some arbitrary steps.

def function_0(x):
	"First function that takes and returns a number"
	return 2 * x
def function_1(x):
	"Second function that takes and returns a number"
	return x ** 2

# Choose which function you want to use.
option = input("Pick function 0 or 1: ")
# Assign one of the functions to another variable.
if (option == "0"):
	to_call = function_0
elif (option == "1"):
	to_call = function_1
else:
	print("Invalid option: " + option)
	exit(-1)

# Run the chosen function.
for x in range(10):
	print("f(%d) = %d"%(x, to_call(x)))

# But you can use it for more than just a complicated if-statement.
