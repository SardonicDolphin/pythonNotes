# Now let's see how Python handles a paradigm that all you Java an C++ people
# should be very familiar with: object oriented programming.
# In object oriented programming,
# you can vary data and functions all at once, and also make changes
# as you go.

# I've already shown objects. But how do you make your own types?
# You define them as classes.
# Think of classes as types, and objects are instances of them.

# What do classes have?
# They have fields, which are data values,
# and they have methods, which are functions
# that work for an object of a particular type.

class BasicClass:
	"This is a basic class, defined from scratch. You can comment it, too."
	# You can assign default values for public and private fields
	# Private fields must start with two underscores
	__private_field = None
	# Otherwise, it's public
	public_field = None
	# Actually, you don't have to predefine them,
	# but then they won't show up for the dir() for the type
	# The default values should be immutable.
	# Remember that you can create an object,
	# say a list, by using the name of the type as a function.
	# What really happens is that you're calling the constructor,
	# which creates the object.
	# It's a special method, of course, called __init__,
	# with underscores around it.
	# Methods always need the "self" parameter,
	# which tells you what object you're using.
	# It's like the "this" variable in Java and C++.
	# But in Python, it's always explicit when you define the method.
	def __init__(self, private_field, public_field):
		"""BasicClass(private_field, public field)
private_field: sets value of __private_field
public_field: sets value of public_field
The "self" argument is automatically included in every call.
It refers to the object itself, like the "this" variable,
in Java and C++, but in Python, it's explicit.
"""
		self.__private_field = private_field
		self.public_field = public_field
	# You can have methods. They use the object's data,
	# and can change it, but they don't have to.
	# For example, str has no methods that change it.
	def __private_method(self, private_field):
		""""private method, which will appear the same way
as private fields"""
		self.__private_field = private_field
	def set_private_field(self, private_field):
		"setter for __private_field"
		self.__private_field = private_field
	def get_private_field(self):
		"getter for __private_field"
		return self.__private_field
	# Here is another special method.
	# This is called when you use "str".
	def __str__(self):
		"like toString in Java, returns string value of object"
		return "%s %s"%(self.__private_field, self.public_field)

print("%s has attributes %s"%(BasicClass.__name__, dir(BasicClass)))
# Actually, "private" is just a suggestion.
# You can still access private fields from outside,
# but you have to prepend it with "_[class name]"

# Like with the built-in classes, the constructor is just the class name.
bco = BasicClass("spriv", "spub")
input()

input()
# You can freely read and change the old public field
print("Before: public_field = %s"%(bco.public_field))
bco.public_field = "pub"
input()
print("After: public_field = %s"%(bco.public_field))

input()
# You should only access private fields using the class methods:
print("Before: __private_field = %s"%(bco.get_private_field()))
bco.set_private_field("priv")
input()
print("Before: __private_field = %s"%(bco.get_private_field()))

# The string representation of the object.
# By default, it's not very readable, but we redefined it.
class NonStringClass:
	def __init__(self):
		pass

input()
nsco = NonStringClass()
print(nsco)
input()
print(bco)

input()
# What if you want another class that is very similar to BasicClass,
# but with some additions?
# You can create subclasses.
# Just include the super class in parentheses in the class declaration.
class SubClass(BasicClass):
	__sub_field = None
	def __init__(self, private_field, public_field, sub_field):
		"""SubClass(private_field, public_field, private_field,
	public field)
private_field: sets value of __private_field
public_field: sets value of public_field
private_field: sets value of __private_field
public_field: sets value of public_field
sub_field: sets value of __sub_field
"""
		# We still need to call the constructor of the super class.
		# How do you call the previous version of the method,
		# if you have overridden it?
		# super(class, object) gives you the
		# superclass version of the object,
		# and lets you call the previous version of the method
		super(SubClass, self).__init__(private_field, public_field)
		# Refer to self object.
		self.public_field = "sub_" + public_field
		# privacy is not inherited.
		# This will create a field for this class
		self.__private_field = "sub_" + private_field

		self.__sub_field = sub_field
	def __str__(self):
		"""Overrides old __str__, but still uses it,
using super again"""
		return super(SubClass, self).__str__() + \
		       " %s %s"%(self.__sub_field, self.__private_field)

sbco = SubClass("priv", "pub", "sub")
print("Instance of class %s has attributes %s"%(type(sbco).__name__, dir(sbco)))
input()
print(sbco)
