# So functions can take arbitrary inputs.
# They also don't have to have the number of return values hardcoded.
# Sure, you can always return a single iterable object.
# But Python has something else for that: generators.

# Let's do a basic iterable over consecutive integers.
def make_range_generator(end):
	i = 0
	while i < end:
		# Here is how this function outputs a generator.
		yield i
		# Notice that yield is not like return.
		# It does not end the function
		i += 1

gen = make_range_generator(10)
# This is the generator type
print("Type: %s" % (str(gen)))
# It has the __iter__ method.
# It doesn't have __len__ or __contain__, though, so it isn't a collection.
print("Attributes of generator: %s" % (dir(gen)))
# So you can see that it goes over the loop where the yield is.
print(list(gen))

# Besides those missing methods,
# how is this iterable object different from a collection?
# When you have a collection,
# you already have all the values that were calculated, if need be,
# and put into the collection.
# That is how you can have a finite length and check for membership.
# That is not true for generators.
# The calculation is done as you iterate.
# Why does this make a difference.
# It makes a difference if there are side effects.

# Let's keep a global variable, and see when it changes.
lazy_count = 0

def make_lazy_generator(end):
	global lazy_count
	i = 0
	while i < end:
		lazy_count += 1
		yield i
		i += 1

input()
lazy_generator = make_lazy_generator(10)
# We already have the generator, but we didn't calculate anything.
print("After making generator, iterated %d times" % (lazy_count))
input()
for generated in lazy_generator:
	print("Iterated %d times" % (lazy_count))
	print("Generated %d" % (generated))

input()
# Now that you think about it, what does "yield" mean?
# In finance, yield is the return you get from a security, like a bond.
# Both yield and return refer to what you get back from some investment.
# So in general terms, yield is just return, and it happens over time.
# But in computer science, they are different.
# In almost every language you'll see, when a function returns, it is done.
# But if you go learn about operating systems or multi-threaded computation,
# a thread, which is kind of like a single instance of a running program,
# yields when it stops running, and lets another thread run,
# kind of like how cars yield on the road.
# A car that yields doesn't stop forever. It just stops going for now.
# So what yield does is stop in the middle of the function, before it finishes,
# let the caller continue, and also give it some intermediate value.
# You don't even have to yield in a loop,
# and you can have separate yields in one function.
def multi_yield(a, b):
	yield "Beginning: I got %d and %d" % (a, b)
	yield "Middle: I will calculate %d + %d" % (a, b)
	result = a + b
	yield "End: The result is %d" % (result)

print("Multiple yields:")
print("\n".join(multi_yield(2, 3)))
