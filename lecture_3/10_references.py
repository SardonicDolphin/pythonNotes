# If you've worked with C before,
# or used static variables in Java,
# you might be wondering. Does Python allow side effects?
# Can you call a function and change the global state?
# The answer is yes and no.
# Normally, just setting the variable to a new value will not help.
# Remember what I showed last time.
# In the local scope, the local variable is distinct.
# It's like getting a new hand to point at an old value.
# If I just point it away, the old hand still points to the same value.

# First, we can look at how that affects the parameter variables.
# Functions in different languages pass parameters by reference or by value.
# If you pass by reference, that means the variable is a reference to a location
# that stores the value.
# So if the function makes an assignment to that variable,
# it is overwrites that location.
# The caller, which has the reference to the same location,
# will see that the variable has changed.
# But Python is what's called passing by value.
# That means that the function's parameter is another variable
# that points to a copy of the value.
# But the value is a reference.
# What does that mean? Remember that everything is an object.
# So the function can't usually change what object the caller's
# variable points to. It's always the same object.
# But something inside the object, like a field, could change.

def change_int(int_param):
	int_param += 1

global_int = 1
print("Before %d"%(global_int))
change_int(global_int)
# What do you think? Will this change, or not?
input()
print("After %d"%(global_int))

def change_list(list_param):
	list_param = [1]

global_list = []

input()
print("Before %s"%(global_list))
change_list(global_list)
# What about a list?
input()
print("After %s"%(global_list))

def append_list(list_param):
	list_param.append(2)

input()
print("Before %s"%(global_list))
append_list(global_list)
# What about now?
input()
print("After %s"%(global_list))

# Why?

# What if you want to, say, have a copy that is changed, but keep the old one?

# The same issue happens with default parameters,
# if the default object is mutable, like a list.
# The default value is only instantiated once,
# no matter how many times you call the function
# without giving the optional paramater.
def bad_call(to_append, default = []):
	default.append(to_append)
	return default

first_bad_call = bad_call("first")
print("First result " + str(first_bad_call))
# So far, so good. Let's call it again, though.
second_bad_call = bad_call("second")
print("Second result " + str(first_bad_call))
# Where did "first" come from.
# Actually, the two results are referring to the same default object
print("First result, after second call " + str(first_bad_call))
print("First result and second result are same? %s" % (first_bad_call is
						       second_bad_call))
# So they are the exact same, even with the "is" operation.
