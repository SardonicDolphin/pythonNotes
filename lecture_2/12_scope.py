# In the first lecture, I mentioned that variables in Python
# can get kind of confusing, compared to other languages.
# But so far, we haven't had a real problem.
# In the first lecture,
# That's because I only showed one scope: the global scope.
# Indentation because of ifs, fors, and whiles don't affect the function.
# What about functions?
# Here's where things get tricky.

conflict = 0

def conflict_function():
	# same variable is used again
	conflict = 1

print(conflict)
# What happens here?
conflict_function()
input()
print(conflict)

# In Python, when you use a variable, it will look in the order:
#	local (declared inside the function)
#	global (declared inside the file, but outside any functions)
#	built-in (always available in the language)
input()
# If you just use the variable, without ever , it'll use the global one.
def just_use_it():
	print("Just using %d"%(conflict))
# If you declare it, the function will use the declared version, instead.
def declare_it():
	conflict = 100
	print("Function redeclared it to %d"%(conflict))
# And it does not matter where you declare it in the function.
# What will happen here?
def declare_it_later():
	print("Will redeclare what is already value %d"%(conflict))
	conflict = 100

just_use_it()
declare_it()
input()
declare_it_later()
