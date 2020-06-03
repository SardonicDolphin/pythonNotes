# Python supports multiple programming paradigms.

# It supports object-oriented programming,
# where you can override common operators.
class ClassExample:
	__field = None
	def __init__(self, field):
		self.__field = field
	def __add__(self, other):
		return ClassExample(self.__field + other.__field)
	def __str__(self):
		return "ClassExample(%s)"%(repr(self.__field))

print("Wrapped addition: %s"%(ClassExample(100) + ClassExample(10)))

# It also supports functional programming.
print("Functional programming lets you use a function as a variable: " +
      " ".join(map(lambda x: str(ClassExample(x)), range(10))))
