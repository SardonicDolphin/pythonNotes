# Scripts make it easy to do complex things without rewriting everything.
# For example, you can create long strings across multiple lines,
# and Python lets you do that, using triple quotes.

# This is a single line comment.

# Block strings can be used as comments, too.
massive = """This is a very long string.
Python will include all the spaces, tabs, and newlines.
Special characters are still translated, though.
Like these line breaks,\n\n\nie.\"\\n\\n\\n\"."""

# Just entering the expression will not print its value.
massive
# print will print the translation of the string.
print(massive)
# repr will show the string as it appears in code
print(repr(massive))

# We can run this using "python3 14_script.py"
