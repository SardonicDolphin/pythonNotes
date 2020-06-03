# Most of the function examples I showed are pretty simple,
# and you might not want to use them again.
# lambda expressions make it easy to generate small functions
# with little boilerplate.
# Their syntax is: lambda [input variable]: output expression

# Let's try the same function as before, but with lambda

for y in map(lambda x: 2 * x, range(10)):
	print(y)
