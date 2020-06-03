# So pickle is a bit risky.
# There is another issue, though, anybody want to guess?
# So have you heard of any substitutes?

# json has functions with the exact same names as pickle.
from json import load, dump, loads, dumps

# It only supports the basic types.
TO_SAVE = {"int": 1, "s": "string field", "b": True, # the "primitive" types
	   "a": [1, 2, 3], "nd": {"n1": 1}} # collections

print("storing %s"%(TO_SAVE))
# The json format is in printable text, so you don't need the "b" flag
with open("json_file", "w") as opf:
	dump(TO_SAVE, opf)

with open("json_file", "r") as ipf:
	loaded = load(ipf)
	# Exactly the same
	print("Loaded from file %s"%(loaded))
	print("old == loaded? %s"%(TO_SAVE == loaded))

input()

# Again, just the string.
json_string = dumps(TO_SAVE)
loaded_from_string = loads(json_string)
print("Loaded from string %s"%(loaded_from_string))
# It's the same.
print("old == loaded? %s"%(TO_SAVE == loaded_from_string))
# And it's perfectly readable.
# Kind of looks like Python, too. It's actually JavaScript.
print("json string: %s"%(json_string))

input()

# Aside from less flexibility, though,
# there are a few issues in terms of translation.
# It only supports string keys, and not tuples.
NOT_PRESERVED = {1: "integer to string key", "tuple": ("tuple to", "list"),
		 "list": ["actual", "list"]}
print("Will try to save: %s"%(NOT_PRESERVED))
not_preserved_string = dumps(NOT_PRESERVED)
print("Saved as %s"%(not_preserved_string))
# See how the tuple and the list are translated to the same format.
changed = loads(not_preserved_string)
print("Loaded as %s"%(changed))
print("old == loaded? %s"%(NOT_PRESERVED == changed))
