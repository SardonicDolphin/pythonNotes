# In Java or C++, you can use the same function name,
# but with different arguments.
# In Python, the function name is also a variable,
# so each name can only have at most one function.
# Luckily, Python functions not only let you vary the values you give it,
# but sometimes, also what values you give it.
# Now, if you give the argument a name, it has to have a value.
# But the caller does not have to give it the value.
# You can give it a default value.
# To be honest, this is much better than how Java or C++ do it,
# because it follows the intuition that the same function name
# does similar things, even if you give it different parameters.

# Here's a function with optional arguments.
def optional_argument(required, optional_1 = 2, optional_2 = 0):
	return (required ** optional_1) + optional_2
# What if I put required after one of the optional arguments?

print("All arguments: %d"%(optional_argument(4, 3, 10)))
input()
print("Only required argument: %d"%(optional_argument(4)))
input()
print("Only first optional argument: %d"%(optional_argument(4, 3)))
input()
# You can skip the second argument, and still assign the third one.
print("Only second optional argument: %d"%(optional_argument(4,
							     optional_2 = 10)))
input()
# Actually, you can just give the names in any order.
print("All arguments, out of order: %d"%(optional_argument(optional_2 = 10,
							   optional_1 = 3,
							   required = 4)))
# Just keep in mind that you have to at least give the required arguments.
# Can I run this?
input()
optional_argument(optional_1 = 3, optional_2 = 10)
