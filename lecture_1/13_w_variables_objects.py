# Let's look at types that you would call "objects" in other languages.
# Actually, everything in Python is an object,
# but the types I show are ones where it helps to use them that way.
# They are complex enough that I don't want to keep typing them.
# Also, some of the objects I will show can be changed,
# but that is only useful if you can reuse the object.
# So I'll start by talking about variables.

# In Python, there is no syntactic difference between variable declarations
# and assignment.
x = 2
# This looks like an assignment in other languages, because there is no type.
# But it is not quite an assignment in Python.
# For one, this is a statement, not an expression,
# which is why it doesn't print a value.
# But in C, an assignment is also an expression
# whose value is the right-hand side.
# Also, it doesn't complain that I haven't declared the variable.
# So what is this? It depends.
# Here, x has not been declared or assigned before,
# so this is actually a declaration,
# and Python will figure out the type for you during runtime.
# Let's use it
x ** 3 # 8
# Now that we've declared it, the next line is an assignment.
x = "A"
x
# Yeah, type does not matter too much, until you start using the value.
x = 3
# Let's try the same expression.
x ** 3 # 27
# You can also change the variable relative to itself, like in C or Java.
# The straightforward way to write it is:
x = x + 1 
x
# The equivalent shortcut is:
x += 1
x
# You can do that with most operations.
# What if I want to set x to be itself, multiplied by 4?

# Now let's look at some more complex objects.
# The types I am showing can all be treated as collections.
# That means you can get their length, and check membership.
# You can also iterate over them, but that's not so convenient to type
# on the console, so I'll show that in a script, later.

# So let's start with ordered collections,
# which are the ones where the elements have indexes.

# Python, like Java, lets you directly work with strings.
"String"
# It doesn't differentiate between strings and characters.
# In other languages, single-quotes are for characters, but not in Python.
'Also a string'
# They start with a backslash. For example a line break.
s = "String\nwith a special character"
# Special characters are shown in their encoded form...
s
# They are translated when you explicitly print them
print(s)
# If you want a quotation mark, you know,
# inside a string that's already surrounded by quotation marks,
# you can put a backslash in front of it.
print("The computer said, \"Hello World\"")
# Anybody want to guess what you write when you want to
# keep a backslash?

# As with Java, Python has the same syntactic sugar -- and then some --
# that makes concatenating strings easy.
"first part" + "second part"
# Multiplication is just repeated concatenation.
"NI!" * 10
# But you can only add a string to a string.
"first part" + 10
# Luckily, every object can be turned into a string. Like this:
"first part" + str(10)

# You can format them directly, without other functions.
# It's like printf in C, or format in Java,
# where you can plug text in the middle of a string.
# If you're familiar with Semitic languages like Arabic or Hebrew,
# you know that you can plug in root letters into a pattern.
# String formatting is a generalization of that.
# You mark the place where you want to plug in text with a percent sign,
# and write a letter for the type.
# "s" is for anything that can be turned into a string -- so anything.
"Hello %s!"%("world")
# "d" if you know it's a number. And you can format multiple arguments.
"Hello %d %s!"%(60, "people")
# What if I try this?
"%d% of all statistics are made up on the spot"%(73)
# You just add another percent sign.
"%d%% of all statistics are made up on the spot"%(86)
# "%" is kind of like syntactic sugar for the format function.
# But it'll look quite different.
# You use curly braces, to mark where you want to plug in the text.
fs = "His name is {} {}."
fs.format("Robert", "Paulsen")
fs.format("Bond,", "James, Bond")
# What's wrong here?
fs2 = "if (1) {\n{}\n}"
fs2.format("return 0;")
# Again, double the special symbols.
fs2 = "if (1) {{\n{}\n}}"
fs2.format("return 0;")

# We're already using a method for string objects.
# You can find the rest like this.
s = "Hello World!"
dir(s)
# Or you can just pass in the type.
dir(str)
# This is immutable, so you can only call accessor methods,
# which are read-only.
# Like create a version of it in all caps.
s.upper()
# Or all lower case.
s.lower()
# Does it start with a certain string?
s.startswith("Hello")
s.startswith("No")
# Does it end with a certain string?
s.endswith("World!")
s.endswith("No")

# But you don't always have to call the methods directly.
# Python makes it very convenient to use special methods:
es1 = "string"
es2 = "string"
es1 == es2
# This would not be true in Java or Python? Why is it here?
dir(e2)
# See those ugly-looking names with the underscores?
[name for name in dir(str) if name.startswith("__")]
# They usually redefine some general feature in the Python language.
# Do you see anything we might have used already?
# So you can actually redefine equality, with __eq__.
# It's like the equals method in Java,
# except the equality operator calls it automatically.
# There is actually another equality operator, "is",
# that you cannot redefine.
# And that's like in Java, where it compares the identity of the objects.
es1 is es2
# This happens to still be true,
# because Python tries to not duplicate a string if the same value
# has already been created.
# But in general, there is only one case where you should use "is",
# and I will show you next time.

# How are strings like ordered collections?
# Let's look at the special methods again.
s2 = "12345"
[name for name in dir(str) if name.startswith("__")]
# They have the __getitem__ method. That lets you use indexing.
# It starts from 0. This is how it's done it most languages.
s2[0]
s2[1]
# So that the last index is 4, which is one less than the size of the string.
s2[4]
# This would cause problems in other languages,
# but in Python, negative just means you're going backwards.
s2[-1]
s2[-4]
s2[-5]
# And not just one integer, but also a range.
# This includes indexes that are at least 2, and less than 4
s2[2 : 4]
# You can leave off the first part, to start from the beginning
s2[ : 4]
# Or the second part, to go to the end
s2[2 : ]
# But, again, it's immutable, like in Java.
s2[2] = "0"

# Let's see how this is like a collection.
[name for name in dir(str) if name.startswith("__")]
# It has __len__, so you can get its length.
len(s2)
[name for name in dir(s2) if name.startswith("__")]
# And it has __contains__, so you can check for membership.
"3" in "12345"
# And the opposite
"0" not in "12345"
# Strings are special for this keyword,
# because you can also use this to test for substrings
"34" in "12345"

# There are other collections, too
# Tuples are like strings. You can index them or slice them,
# yet they're immutable.
# They're used for if you want to put a few values together,
# but don't want to use objects --it's a bit more work,
# and I'll talk about it next lecture.
# Tuples have parentheses around them,
# as if you just wanted to put them together,
# or nothing at all.
# Again, they're ordered collections
t = ("1", 2)
tn = "1", 2
t
tn
t[0]
t[1]
t[0] = 0
(1, 2, "3", "4", 5)[2 : 5]
# Again, you can also concatenate and multiply them
t + (7, 8)
t * 4
# And the usual collection expressions
len(t)
2 in t
# Also notice that type doesn't matter too much,
# as long as you don't try anything too type-specific later.
# That makes it easy, but you could easily make a mistake
# that doesn't get caught until runtime.
# This time, "is" does not work like __eq__
t2 = ("1", 2)
t is t2
t == t2

# Lists have all the functionality of tuples.
# But you define them with square brackets.
l = ["1", 2]
l
l[0]
l[1]
[1, 2, 3, "4", "5"][2 : 5]
l + [3, 4]
l * 4
# And now you can change it
dir(l)
# You can change one entry, because it has __setitem__
l
l[0] = 0
l
# You can add something on the end, with append:
l.append(900)
l
# Insert something at a certain position.
# 2 is the position. 800 is the value.
l.insert(2, 800)
l
# If you go overboard with the index, it'll just put it at the end.
l.insert(99999999999, -1)
l
# If the index is too negative, it'll put it at the beginning.
l.insert(-99999999999, -2)
l
# You can also delete. The function is __delitem__,
# but Python lets you just type del:
del l[2]
l

# The rest is the same
# What is this?
len(l)
# Is this True or False?
0 in l
l1 = [1, 2]
l2 = [1, 2]
# True or False?
l1 is l2
# True or False?
l1 == l2

# Let's move on to some collections that are not indexed, but pretty powerful.
# Dictionaries let you look up values with a key, which must be immutable.
# In other languages, they are usually called hash maps.
# You create them with curly braces,
# and show the key-value pairs with colons.
d = {"a": 1, "b": 2}
# Here, you can only look up one key at a time
d["a"]
d["b"]
# Replace one
d["b"] = 200
d
# Or create a new one
d["c"] = 3
d
# But watch out, if you try to get a key that does not exist
d["e"]
# For dictionaries, "in" refers to the keys only,
# so you can check if the key exists.
"e" in d
"b" in d
# If you're in Python 2, has_key does the same thing
d = {"a": 1, "b": 2}
d.has_key("e")
d.has_key("b")
# Again, you can delete.
del d["a"]
d

# At the risk of being repetitive.
d1 = {"hundred": 100, "thousand": 1000}
d2 = {"thousand": 1000, "hundred": 100}
# True or False?
d1 is d2
# True or False? Even with the order?
d1 == d2

# The last unordered, built-in collection I'll talk about today is the set.
# A set is like the set in the mathematical sense,
# and Java has a similar object with the same name.
# It's not ordered,
# and what matters is just if a member exists in the set or not.
# When you want to create a non-empty set,
# you use curly braces, just like a dictionary,
# but you don't have any key-value pairs.
# Just write it like a list of values, but with curly braces.
st = {1, 2, 4, 8}
st
# It's mostly used for checking membership, with "in":
1 in st
3 in st
# You can also do your usual set operations, with normal methods.
[name for name in dir(set) if not name.startswith("__")]
st2 = {4, 8, 16}
st.union(st2)
st.intersection(st2)
# Sets are also mutable
# You can add a single element
st.add(32)
st
# Or remove it,
# but because there's no index or key, you have to remove the element itself.
# There is no special method for that. You just call remove directly.
st.remove(32)
st
# You can also add a whole collection --any collection -- of elements
st.update([3, 9, 27])
st
sta = {1, 2, 3}
stb = {3, 2, 1}
# True or false?
sta is stb
# True or false?
sta == stb

# So, I kind of glossed over two things there.
# First. What if you want an empty set?
# If you have nothing between curly braces, you just have a dictionary.
type({})
# You can use the more standard way, of using the set object constructor,
# which is just the name of the type -- you don't need to write "new",
# like you have to in Java or C++. It's like a function.
# In fact, I've already shown a standard-looking constructor.
# Can anybody guess which one?
# Now, for set, the only parameter is another collection:
set([])
# That brings me to the second point I need to elaborate on, which is:
# How do you convert from any collection to a set?
# You've seen it in update. Now you see it in the constructor.
# There is another property of collections I have not explained: iterators
# It's mostly useful for loops.
# But it's also used for creating collections out of other collections.
# All collections have an __iter__ function,
# which gives you an iterator, like the iterable classes in Java and C++
"__iter__" in dir(set)
"__iter__" in dir(tuple)
"__iter__" in dir(list)
"__iter__" in dir(dict)
"__iter__" in dir(str)
# We already know that str takes any object,
# because every object has the __str__ method.
# On the other hand, set, list and dict have to take something that is iterable.
# Let's see what if you don't.
set(1)
tuple(1)
list(1)
dict(1)
# So. Let's say we want some collection with 1, 2, 2, 4
base = [1, 2, 2, 4]
set(base)
# Notice that 2 only appears once. That's because sets don't care about repeats.
tuple(base)
lc = list(base)
lc
# We created a list from another list.
# Because lists are mutable, this is actually another copy.
lc is base
# That way, you can change one, without changing the other
lc.append(5)
lc
base

# Now, this won't work with dictionaries. You have to do something more.
dict(base)
# You need to give it a collection of pairs,
# which could be any collection of length two.
# The first element in the pair is the key. The second is the value.
d = dict([(1, 2), (3)]
d = dict([(1, 2), (3, 4, 5)]
d = dict([(1, 2), (3, 4)]
d
# Or you can give it another dictionary. This'll make a new copy,
# like with copying lists.
dc = dict(d)
dc is d
# Iterating over dictionaries also is a little different.
# It just goes over the keys.
list(d)
# If you just want a collection of the values, use the values method
values = d.values()
values
# If you want all the pairs, use the items method
items = d.items()
items

# Do be careful, though. In Python 3, if you change the dictionary,
# the values and items it returned to you already will change.
# Not in Python 2. Those are just new lists.

# One other shortcut you can take with collections
# is declare or assign multiple variables at the same time.
# You can do this if your left hand side is a tuple or list of only variables,
# and the right hand side has the same length as the left hand side:
# Remember base? It has four elements.
base
a, b, c, d = base
a
b
c
d
# One thing you can do is easily swap variables:
a, b = b, a
a, b

# If you want to split a string, using the split method,
# and you know how many parts it will have,
# you can assign it to relevant variables.
# Usually, splitting gives you a list.
ss = "split me"
ss.split(" ")
part_a, part_b = ss.split(" ")
part_a, part_b
# When we talk about functions and return values,
# this trick will be more useful.
