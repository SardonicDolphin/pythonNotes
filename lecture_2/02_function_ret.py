# A function in programming is not always like a mathematical function.
# First of all, a mathematical function always gives you a value.
# So far, the functions I wrote only print something.
# In Python, you return the value with return.
# It's the same as Java and C.

# A simple function that returns a single value.
def ret_function(x):
	y = x * x
	return y

print(ret_function(4))

input()

# What if you want to return multiple values?
# You can return any collection. A tuple is the simplest.

def return_many(dividend, divisor):
	quotient = dividend // divisor
	remainder = dividend % divisor
	# You just put commas between the values you want to return.
	return quotient, remainder

dividend = 19
divisor = 3

print("return_many(%d, %d) = %s"%(dividend, divisor,
				  return_many(dividend, divisor)))

# So I can get a collection of return values.
# That's useful. But what I want to use each return value separately?
# Here is where splitting collections into variables is useful.
# You know that return_many returns two values,
# so you can break it into a tuple of two values
returned_quotient, returned_remainder = return_many(dividend, divisor)
# You can also try a list.
[returned_quotient, returned_remainder] = return_many(dividend, divisor)
# We can immediately put the values to use, without having to access the tuple.
print("%d * %d + %d = %d"%(returned_quotient, divisor, returned_remainder,
			   dividend))
