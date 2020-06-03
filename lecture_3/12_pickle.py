# Python also makes it easy to store some pretty complicated stuff in files.
# But the easiest way to do it is not the best way.

# The easy way is pickle.
# It lets you store basic types and some arbitrary objects.
# It's pretty flexible, but that's what makes it dangerous.

from pickle import load, dump, loads, dumps

from time import localtime

# Let's try to pickle a dictionary.
# It can have any built-in types, and any objects that support pickling.
TO_PICKLE = {0: 1, 0.0: 3.14, "s": "string field", # the "primitive" types
	     "a": [1, 2, 3], "t": (-1, 1), "nd": {"n1": 1}, # collections
	     "time": localtime()} # object

print("Pickling %s"%(TO_PICKLE))
# You can write it directly to a file,
# but you need an extra flag, "b", to say that the data will be binary.
# In Python 3, that makes a difference,
# since the pickle data will not be human-readable.
with open("pickle_file", "wb") as opf:
	dump(TO_PICKLE, opf)

# And load it, again with the extra "b" flag.
with open("pickle_file", "rb") as ipf:
	loaded = load(ipf)
	# Exactly the same
	print("Loaded from file %s"%(loaded))
	print("old == loaded? %s"%(TO_PICKLE == loaded))

input()

# If you don't want to save it to a file, just yet,
# you can use dumps and loads. "s" stands for string.
# That's a legacy of Python 2. In Python 3, it's actually bytes.
pickled_string = dumps(TO_PICKLE)
loaded_from_string = loads(pickled_string)
print("Loaded from string %s"%(loaded_from_string))
# It's the same.
print("old == loaded? %s"%(TO_PICKLE == loaded_from_string))
# I just wanted to show you, though, what the pickled data looks like.
# That's why you want to save it in binary form.
print("pickled string: %s"%(repr(pickled_string)))

input()

# I said that it only works for objects that support pickling.
# You can actually make any object support pickling,
# by defining the __reduce__ method,
# but that's the reason you don't want to use pickle.
# The reduce method returns a function and the parameters you want to give it
# during unpickling. Of course, the function could do a lot of things.
# Like cause an error.
def something_nasty():
	return 1 / 0
class BadPickle:
	def __reduce__(self):
		return (something_nasty, ())

bad_pickled_string = dumps(BadPickle())
input("Saved bad object: %s"%(repr(bad_pickled_string)))
loads(bad_pickled_string)

# The lesson is, if you don't trust where the pickled data is coming from,
# don't load it.
# This applies to things you get from other programs.
# You might still be able to use pickle if you're absolutely sure
# that no other program can change the file.
