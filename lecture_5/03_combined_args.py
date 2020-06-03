# Let's put the two together. This lets you accept all kinds of parameters.

def combined(*ordered, **named):
	for arg_i in range(len(ordered)):
		print("%d: %s" % (arg_i, ordered[arg_i]))
	for (name, value) in named.items():
		print("%s = %s" % (name, value))

combined(0, 3, u0 = "a", u1 = "b")

# It's no accident that I put ordered before named.
# If I switch the order, that's not even correct syntax.
# If I give one of the earlier arguments a name, that's also an error.
