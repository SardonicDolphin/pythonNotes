# Right now, everything's been self contained,
# except for standard input and output.
# But to be able to do anything useful with Python,
# you will need other ways of interacting with your scripts.
# There are many other ways for the user to interact with your script.
# The first one we'll look at is sys.argv

from sys import argv

# In C, you've probably seen "argv" in the main function.
# In Java, you have "args" in the main method.
# What it does is take the text you give it into the command line,
# and gives it to the program in a list.
# In Python, it's as easy as Java's "args",
# but it uses the indexing in C.

print(argv)
# You see, it starts with the actual program, not the first argument.
# "python3" is not included, though.

# We could try assigning the values, if we know how many there are
if (len(argv) == 3):
	# Let's try it with 3
	(command, argument_1, argument_2) = argv
	print("You ran %s with %s and %s"%(command, argument_1, argument_2))
else:
	# If we didn't give it the right number of options
	print("You did not give 2 command line options")
# But that's going to be a pain to use.
# If you're familiar with running other programs through the command line,
# then you probably know that they let you put arbitrary flags
# in arbitrary places.
