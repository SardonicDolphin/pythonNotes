# You can use the Python console as a calculator.
# When you enter values and expressions,
# the console will evaluate it, and print it back to you, automatically.
# Let's look at the values and expressions you can write in Python

# Python supports basic arithmetic operations:
2 + 3 # 5
3 - 2 # 1
2 * 3 # 6
# Like most languages, there are also bitwise and discrete math operations:
# Bitwise operations have to do with the fact that numbers
# are represented in binary.
# Not too useful unless you already know what they mean.
# If you do know about bits, the idea is that they can get shifted around,
# and have logical operations performed bit-by-bit.
5 << 1 # Bit shifting. Right bit shift is like multiplying by a power of 2
5 >> 1 # Bit shifting. Left bit shift is like dividing by a power of 2,
#	 but rounded down.
5 & (1 << 2 | 1 << 1) # Bit shifting, ORing and masking: 5 & 3 = 4
# The modulo operation also exists in Python
7 % 4 # Calculate the remainder: 3

# Python's always been trying to make the math more useful for real life,
# which is not quite how most other languages,
# or even older version of Python do it.
# Division is real-number by default in Python 3, but not in Python 2
# If this were C or Java, what would this be? What about Matlab? R?
# Now, what about Python?
7 / 4
# Use // to round down. This even works with real numbers
7 // 4 # 1
7.0 // 4.0 # 1.0
# Python also supports exponentiation without extra functions
3 ** 4 # 81

# Python's logical operations are specifically made for booleans
False and True # False
False or True # True
# Exclusive ORs are like other languages. That means exactly one is true
False ^ True
# Like && and || in C and Java, these operations short-circuit.
# So if the answer is already known from the left operand,
# the right operand is not evaluated.
# This will be important once you can change things.
not False # True

# The comparison operations you use for other types return booleans.
# You need two equal signs.
1 == 1
4 == 2
# Some different types can even be compared
3.0 == 3

# Of course there are the other comparison operations
4 != 2 # Not equals, with the exclamation mark like in other languages
4 > 2 # Strictly greater than
4 >= 2 # Greater than or equal to
2 >= 2
4 < 2 # Strictly less than
4 <= 2 # Less than or equal to
4 <= 4
# If you're not familiar with the comparison symbols,
# just remember that if you have the equals sign, it is on the right side.
