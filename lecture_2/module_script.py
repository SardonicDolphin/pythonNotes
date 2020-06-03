# I said in the first lecture that you can run Python directly,
# without any main method or function.
# So what happens if you want to run a module as a script?
# The modules I've shown only have definitions.
# But you can run them as a script, and have them do things.
def do_nothing(x):
	return x + 1

# This code will actually be executed.
print("Use the module function: %d"%(do_nothing(1)))
