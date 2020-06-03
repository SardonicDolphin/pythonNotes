# Now here is something that Python does that most other languages don't.
# You remember how I showed that you can put arguments in different orders,
# if I give their names.
# What data structure could do that?

# Now you have two stars.
# Think of it as representing unknown name-value pairs,
# while before, you only had unknown values.
def get_named_args_type(**mystery_type):
	print("Named arguments are of type %s" % (type(mystery_type)))

get_named_args_type(first = 0, second = 1, third = 2)

input()

# So we can treat it as such.
def named_args(**named_args):
	for arg_name, arg_value in named_args.items():
		print("%s = %s" % (arg_name, arg_value))

named_args(first = 0, second = 1, third = 2)
