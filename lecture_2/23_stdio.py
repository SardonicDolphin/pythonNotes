# In fact, you've already been working with files.
# They are standard input, and standard output.

# You can explicitly import them from the sys module.
from sys import stdin, stdout

# You can read lines from the standard input stream.
# It's like input, but without the prompt:
in_line = stdin.readline()
# You can print it using the standard output stream.
print(repr(in_line), file = stdout)
# That's just the default behavior of print
# Because you pressed enter, there's always going to be a new line character.
# Usually, you won't need that.
# Luckily, there is rstrip, which makes a copy of the string,
# with all whitespaces at the end removed.
print("Stripped: %s"%(repr(in_line.rstrip())), file = stdout)
# And I mean all whitespaces, not just newline.

# There is another output stream: the standard error stream.
# It's printed out when there is an error.
# You mostly notice the difference in C or C++,
# where it is more robust.
# When you try to pipe out the output,
# you'll also see that they're different.
# To pipe out the standard output, just put ">" and the output file name
# after the command
# To pipe out the standard error, also put "2" in front of the ">".
from sys import stderr
print("Error", file = stderr)
