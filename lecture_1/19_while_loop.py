# Sure, sometimes a break will stop the for loop ahead of time.
# But it's generally predictable. You have a maximum limit for when it'll end,
# and there is a predetermined order.
# What if you don't know what you'll do next until you get there,
# and there is no predetermined order?
# You use a while loop. It means you keep repeating while the condition is true.
input_str = input("Enter your starting number: ")

if input_str.isdigit():
	input_int = int(input_str)
	if (input_int > 0):
		current_value = input_int
		# We don't know when we will hit 1, but stop when we do
		# How else can we write this while loop?
		while input_int != 1:
			print(input_int)
			if input_int % 2 == 0:
				input_int //= 2
			else:
				input_int = 3 * input_int + 1
			if input_int == 1:
				print("Reached 1!")
	else:
		print("%d is not a positive integer"%(input_int))
else:
	print("%s is not a valid integer"%(input_str))
