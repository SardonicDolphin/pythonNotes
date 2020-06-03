#03_w_regex_syntax.py

# I'll end today by talking about regular expressions.
# They're a somewhat more flexible way
# of finding and replacing text.
# Where does it come in handy?
# If you're searching in a file, of course.
# But it's also useful if you want to write a web service using Django,
# because it uses regular expressions to parse URLs.

# It's a very important part of the Perl language.
# It's also available in Java,
# but you have to fight through the API.
# Python is a cross between the two.
# There is just enough built-in support,
# so that it doesn't involve lots of hoops,
# but you can use the intuitive Python style.

# Like in Java regular expressions,
# you have to compile a string into a regular expression object.

# So let's get started with the function you'll always need.
from re import compile
# This turns a string into a regular expression object.
simple = compile("abc")
print(type(simple))
# This gives a regular expression, "abc".
# What does this actually do?
# The most basic thing you can do with a regular expression is search.
# That's the method for searching inside a string
# for matches to the pattern.
# What do I mean by matches? That's up to the regular expression string,
# that we gave to compile.
# If you have a string of regular characters,
# then this is equivalent to searching for a substring that matches exactly.
m = simple.search("0123abcd")
# If it matches, then you get an object.
# Let's see what it does.
# span shows you the matching range.
m.span()
# What do you think these numbers mean?
# If there is no match, then it returns None.
print(simple.search("0123acd"))

# But regular expressions are more than just glorified searches.
# You can also give it flexibility.
# The first operation I'll show you in regular expressions is the pipe sign.
# That looks like a bitwise OR. And it acts like OR.
# It can match the expression on either side.
# Let's say you're looking for mentions of either Superman or Clark Kent.
hero = compile("Superman|Clark Kent|bird|plane")
print(hero.search("This looks like a job for Superman"))
print(hero.search("Mild-mannered Clark Kent"))
print(hero.search("It's a bird, it's a plane, it's Superman!"))
# A word about operator precedence. What do you think comes first,
# concatenation or OR?
# Not that easy to remember. So you can use parentheses.
# Say you have two people with the same first name,
# but different last names. You would put parentheses around the last names.
mothers = compile("Martha (Kent|Wayne)")
mothers.search("Martha Kent")
mothers.search("Martha Wayne")

# The next primitive operations have to do with repetition.
# There are two kinds.
# "*" lets you repeat zero or more times.
# Think of multiplication.
# When you multiply a string by 0, you get the empty string.
ha = compile("(ha)*")
ha.search("hahaha")
ha.search("")
# "+" lets you repeat in addition to the first copy.
# Adding strings never gives you anything shorter.
la = compile("la+")
la.search("lalala")
la.search("")
# Now the repetition does not have to be exact.
Ha = compile("((H|h)a)*")
Ha.search("HahaHa")

# In theory, now you can match anything.
# But there's more.
# For one, there is a slightly more convenient syntax
# for matching from a set of characters.
# You just put it in square brackets.
# We can create the same regular expression as above.
Ha2 = compile("([Hh]a)*")
# You just put the characters together.
Ha2.search("HahaHa")

# But you don't have to type all of the characters.
# For example, if you want to match the first 6 non-zero digts,
# you can put a dash between them.
some_numbers = compile("[1-6]")
some_numbers.search("2")
# You can combine both forms.
# Say you want to represent all of the hexadecimal digits.
hex_digits = compile("[a-fA-F0-9]")
hex_digits.search("1b")

# Or you can match everything except for the characters,
# with a caret sign.
not_some_numbers = compile("[^1-6]")
not_some_numbers.search("1")
not_some_numbers.search("A")

# There are some special character classes where you don't have to use brackets,
# although you can put them in brackets.
# "." is the ultimate wild card. It includes everything, except for new lines.
something = compile(".+")
something.search("everything")
something.search("\n")
something.search("everything\nnothing")

# Now we have some special characters with backslashes.
# And you put backslashes in front if you actually want backslashes.
# What's the problem here?

# Luckily, Python has another kind of string,
# and it makes matching regular expressions easy.
# What's the problem now?
# Actually, the compiler interprets slashes as escapes,
# even though it's not used as one in the string.
# So you can write everything else like normal.
# You just put the letter "r" in front of your string,
# and it will be interpreted so that all backslashes are kept.
# "r" stands for raw, but you can also remember that it's used for
# regular expressions.

slash = compile("\\")
slash = compile(r"\\")
slash.search("\\")
# If you really wanted to type that out as a normal string,
# it would look a little messy.
slash

# We did not actually have to use the 0-9 in the square brackets for digits.
# "\d" does it for you.
digit = compile("\d")
digit.search("1")
# "\D", with a capital D, is everything, is the negation,
# like having the caret sign in the square brackets.
not_digit = compile("\D")
not_digit.search("1")
not_digit.search("a")

# "\w" means word characters. What's that?
# That's all numbers and letters, and underscore.
# Why is that special?
# That's all the characters you can use in variable names,
# except for the first character, which cannot be a number.
word = compile("\w")
word.search("1")
word.search("a")
word.search("_")
# So how would we write a regular expression to match a variable name?

# What if we want to match everything except for word characters?

# The last special character class is for any spaces.
# Single space, new line, tab, return.
space = compile("\s")
space.search(" ")
space.search("\t")
space.search("\n")
space.search("\r")

# What is everything except for spaces?

# There are also operations to keep the repetition under control.
# You can use curly braces to say how many repetitions you want.
# If you just have a single number, that means exact repetition
ha_3 = compile("(ha){3}")
ha_3.search("ha" * 3)
ha_3.search("ha" * 2)
ha_3.search("ha" * 4)

# If you have two numbers, separated by a comma, that gives you a range.
ha_2_4 = compile("(ha){2,4}")
ha_2_4.search("ha" * 1)
ha_2_4.search("ha" * 2)
ha_2_4.search("ha" * 3)
ha_2_4.search("ha" * 4)
ha_2_4.search("ha" * 5)

# If you leave the first number empty, it's assumed to be 0.
# In other words, you only have an upper bound.
ha_max_2 = compile("(ha){,2}")
ha_max_2.search("ha" * 0)
ha_max_2.search("ha" * 1)
ha_max_2.search("ha" * 2)
ha_max_2.search("ha" * 3)
# notice how it matches, but not everything.
# We'll take care of that later.

# If you leave the second number empty, there is no upper limit,
# only a lower limit.
ha_min_2 = compile("(ha){2,}")
ha_min_2.search("ha" * 0)
ha_min_2.search("ha" * 1)
ha_min_2.search("ha" * 2)
ha_min_2.search("ha" * 3)

# "?" has two meanings. By itself, it means whatever comes before it
# either does not appear at all
# In other words,
# the question mark means you're not sure if a pattern will appear at all.
maybe = compile("h?")
maybe.search("")
maybe.search("h")

# If it's directly after "+", "*", or the curly brace operation,
# with no closing parentheses in between,
# then it means, don't be greedy.
# You might have noticed that for repetitions,
# it tries to match as much as it can. That's called greedy.
# With the question mark, it's non-greedy.
ha_non_greedy = compile("(ha)+?")
ha_non_greedy.search("ha" * 4)
# Just one "ha"

# The next two characters are for another purpose.
# When caret is outside of the square brackets,
# it means that the string must start with the pattern.
start = compile("^h")
start.search("ha")
start.search("aha")
# The dollar sign means that the string must end with the pattern.
end = compile("a$")
end.search("ha")
end.search("hat")
