#04_w_regex_methods.py

# There are other methods in the regular expression object.

from re import compile

# The next simple method is match.
# That matches from the start, so the caret sign is redundant, in that case.
to_match = compile("h")
to_match.match("ha")
to_match.match("aha")

# The findall method, as it name suggests, tries to find all matches.
# Let's match all the letters.
letters = compile("[a-zA-Z]+")
letters.findall("It was the best of times, it was the worst of times.")
# So we get a list of all the words.

# Lets try something a bit different.
letters_2 = compile("([a-zA-Z])([a-zA-Z]*)")
# Is this the same as the last pattern?
letters_2.findall("It was the best of times, it was the worst of times.")
# We've got tuples. Where do they come from?
# Turns out parentheses are for more than just ordering the operations.
# They also let you extract parts of the match.
# If you used the regular search method,
# you can get the so-called group, whose index is ordered by something
# called pre-order.
m = letters_2.search("It was the best of times, it was the worst of times.")
# The top level
m.group(0)
# The next two levels
m.group(1)
m.group(2)
# This doesn't exist.
m.group(3)
# If you remember this from data structures, fine.
# If you don't don't worry.
# Python makes it easy to keep track of the groups.
# You can give them a name. Just put ?, P, and the name in angle brackets.

# Like if we want to get parts of an email.
grouped = compile("(?P<name>.*)@(?P<server>.*)")
m = grouped.search("yuanjk@cs.columbia.edu")
m.group("name")
m.group("server")

# The last major thing you can do with regular expressions is substitution.
# You can replace parts of a string.
original = "do did done deed dead"
# Say we want to take away all of the vowels in the sentence.
vowels = compile("[aeiouAEIOU]")
# We call the sub method, with the thing new string we want to put in,
# and the original string.
vowels.sub("", original)
# By the way, what is the original string?
original
