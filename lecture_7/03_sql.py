# Now let's start doing something with the data.
from sqlite3 import connect

# Connect again, and get the cursor.
connection = connect("subways.db")
cursor = connection.cursor()

# To get data, use SELECT.
# "SELECT * FROM" and then name is the most simple one.
# It gives you the full rows of every table.
cursor.execute("SELECT * FROM locations")
# But you just executed the command. How do you get the data?
# You use fetchall, which gives you a list of tuples.
results = cursor.fetchall()
input("Whole database: %s" % results)
# Each tuple contains the four columns: the ID, name, longitude and latitude.

# What if you just want the name and location?
cursor.execute("SELECT name, latitude, longitude FROM locations")
less_columns = cursor.fetchall()
# Now we have only the columns we want in a tuple.
input()
print("Just the chosen columns")
for name, latitude, longitude in less_columns:
	print("%s:\n\t%f\n\t%f" % (name, latitude, longitude))

# Just like you can select only some elements using list comprehension,
# and from slicing in pandas,
# you can choose what rows you select in SQL.
# Let's select all of the 1 line stations.
# To make a selection, you also add WHERE, and some logical expressions.
# It's a lot like Python, except you use single equals.
# Why do you think that is?
input()
print("Just the stations on line 1")
cursor.execute("SELECT id FROM station_line WHERE line = ?", '1')
just_1 = cursor.fetchall()

for object_id in just_1:
	print("\t%s" % (object_id))

input()
# Or all the stations on lines 1 and A.
# You use the OR operator. It can be capitalized, but it doesn't have to be.
print("Just the stations on lines 1 and A")
cursor.execute("SELECT id FROM station_line WHERE line = ? OR line = ?",
	       ('1', 'A'))
just_1_a = cursor.fetchall()
for object_id in just_1_a:
	print("\t%s" % (object_id))
print("That was both lines 1 and A.")
# That's a lot more lines.
# But what if you just want the stations whose numbers are less than 100?
input()
print("Just the stations on lines 1 and A less than 100")
cursor.execute("SELECT id FROM station_line WHERE (line = ? OR line = ?) " +
						  "AND (id < ?)",
	       ('1', 'A', 100))
just_1_a_low = cursor.fetchall()
for object_id in just_1_a_low:
	print("\t%s" % (object_id))
# Why do you think I put the parentheses there?

# So we have the station ID's, but it's not very helpful. We want the names.
# If this data was in Pandas, what would we use?
# For SQL, it's called join. And there are a few variations.
# There is inner join
input()
print("Inner join")
# You write INNER JOIN between the two tables,
# and after ON, you say the condition where you combine two rows
# from each table.
# But here, to differentiate between the two 'id' columns,
# you explicitly say which table's column you use.
# It's kind of like left_on and right_on.
cursor.execute("SELECT name, line from station_line INNER JOIN locations ON " +
	       "station_line.id = locations.id")
inner_join = cursor.fetchall()
for object_id, line in inner_join:
	print("\t%s is on line %s" % (object_id, line))
print("That was an inner join")
# If you look at the results, one of the stations is the fake station. Why?
# If you want to show the fake station, how would you show it in pandas?
# In sqlite, unlike other flavors of SQL, you only have left outer join.
# But that's good enough if we want to show the fake station.
# So replace "INNER JOIN" with "LEFT OUTER JOIN",
# and put table with the fake station on the left side.
input()
print("Left join")
cursor.execute("SELECT name, line FROM " +
	       "locations LEFT OUTER JOIN station_line ON " +
	       "station_line.id = locations.id")
left_join = cursor.fetchall()
for object_id, line in left_join:
	print("\t%s is on line %s" % (object_id, line))
print("That was a left join")
# As you can see, the fake station is at the end, and it has None for the line.

# That's a lot of data.
# Maybe you're not so convinced that the first join
# did not have the fake station.
# There are two ways we can show that.
# The first is to take advantage of the inner join's ON condition.
# All rows in the result must satisfy that condition,
# which doesn't just have to be about columns matching.
input()
print("Inner join with another condition")
cursor.execute("SELECT name, line from station_line INNER JOIN locations ON " +
	       "station_line.id = locations.id AND name = ?", ('fake',))
# By the way, we're using parameterization again,
# and I put a comma at the end of the tuple,
# otherwise Python thinks I'm just trying to control the order of operations.
conditioned_inner_join = cursor.fetchall()
for object_id, line in conditioned_inner_join:
	print("\t%s is on line %s" % (object_id, line))
# Nothing there.
# Let's try the same thing for the left join.
input()
print("Left join with another condition")
cursor.execute("SELECT name, line FROM " +
	       "locations LEFT OUTER JOIN station_line ON " +
	       "station_line.id = locations.id AND name = ?", ('fake',))
conditioned_left_join = cursor.fetchall()
for name, line in conditioned_left_join:
	print("\t%s is on line %s" % (name, line))
print("That was a left join with an extra condition")
# Why doesn't this work?
# What can you do?
# Turns out the result of a join is like a new, but temporary, table.
# So you can also use WHERE on it.
input()
print("Left join with WHERE")
cursor.execute("SELECT name, line FROM " +
	       "locations LEFT OUTER JOIN station_line ON " +
	       "station_line.id = locations.id WHERE name = ?", ('fake',))
where_left_join = cursor.fetchall()
for name, line in where_left_join:
	print("\t%s is on line %s" % (name, line))

# If you had a choice, like for the inner join, which one is better?
# For large data sets, having the condition inside the ON part is faster,
# because rows that don't satisfy what you want will be filtered out earlier.

# Now let's use join for what we really wanted, which was look for all stations
# on line 1.
input()
print("Names of stations on line 1")
cursor.execute("SELECT name, line FROM station_line INNER JOIN locations ON " +
	       "station_line.id = locations.id AND line = ?", ('1',))
named_line_1 = cursor.fetchall()
for name, line in named_line_1:
	print("\t%s is on line %s" % (name, line))

# There are other things you can do with tables, including ones from join.
# One of them is grouping. Where have you seen this before?
input()
print("Number of lines at each station")
# You don't just select a column this time.
# You also get an aggregate statistic of the grouped cells of the line column.
# What does this look like?
cursor.execute("SELECT station_line.id, name, count(line) " +
	       "FROM station_line INNER JOIN locations ON " +
	       "station_line.id = locations.id GROUP BY station_line.id")
grouped_by_station = cursor.fetchall()
for object_id,  name, n_lines in grouped_by_station:
	if n_lines > 1:
		suffix = "s"
	else:
		suffix = ""
	print("\t%s (%d) has %d line%s" % (name, object_id, n_lines, suffix))

# Where does WHERE go?
# First, do you even want to use WHERE?
# If you're using an outer join,
# and want to filter out the results of the joined result,
# then it is a good idea to use it.
# Put it before GROUP BY.
# This is a case where you want WHERE.
# You want to only show stations whose IDs are at least 450,
# and that includes the fake station, so you want to use a left join.
input()
print("Number of lines at each station with ID at or above 450")
cursor.execute("SELECT locations.id, name, count(line) " +
	       "FROM locations LEFT OUTER JOIN station_line ON " +
	       "station_line.id = locations.id " +
	       "WHERE locations.id >= ? GROUP BY station_line.id", (450,))
# I changed a few things for the left join. Why?
grouped_where = cursor.fetchall()
for object_id,  name, n_lines in grouped_where:
	if n_lines != 1:
		suffix = "s"
	else:
		suffix = ""
	print("\t%s (%d) has %s line%s" % (name, object_id, n_lines, suffix))

# But what if we want to look at only stations
# where you can transfer between lines?
# You'll need to get the number of lines to see if some station
# has more than one line.
# So intuitively, you put it after the GROUP BY,
# but you use the keyword HAVING
input()
print("Stations with more than one line")
cursor.execute("SELECT locations.id, name, count(line) " +
	       "FROM locations INNER JOIN station_line ON " +
	       "station_line.id = locations.id " +
	       "GROUP BY station_line.id HAVING count(line) > ?", (1,))
grouped_having = cursor.fetchall()
for object_id,  name, n_lines in grouped_having:
	print("\t%s (%d) has %s lines" % (name, object_id, n_lines))
print("All stations have at least 2 lines.")

# For operations you can do on a bunch of rows, look at:
# https://www.techonthenet.com/sqlite/functions/index_alpha.php

# We can get the average longitude for each line for example.
input()
print("Average longitude")
cursor.execute("SELECT line, avg(longitude) " +
	       "FROM locations INNER JOIN station_line ON " +
	       "station_line.id = locations.id " +
	       "GROUP BY line")
line_longitude = cursor.fetchall()
for line, avg_longitude in line_longitude:
	print("\t%s is on average %f degrees West" % (line, -avg_longitude))

# You can also use it in a normal select,
# if you just want a single aggregate,
# like the minimum longitude.
# This is one of the few times I ran the fetchone method, not fetchall,
# because we only expect one output.
cursor.execute("SELECT min(longitude) FROM locations")
most_west = cursor.fetchone()
# But it's still a tuple.
print("The furthest station west is at %f degrees West" % (most_west[0]))

# We can also make changes. You use the UPDATE command.
# Let's change the location of the fake station,
# and set its latitude and longitudes to 0.
# Here it is originally.
# That's a lot of data. But how about you just are looking for one row?
# Say we want the fake row, which we gave an ID, one.
input()
print("Fake station, before the change")
# We SELECT, again, and we know it has the ID 500.
cursor.execute("SELECT * FROM locations WHERE id = ?", (500,))
before_change = cursor.fetchall()
for row in before_change:
	print("\t%s" % (row,))

# Then we use the UPDATE command.
# You give it the table name, then SET,
# and then pairs of the column names, and the new values.
# We can choose which columns we want to change using WHERE again.
# So you can change multiple rows all at once, so be careful
# about what your conditions are.
cursor.execute("UPDATE locations SET latitude = 0, longitude = 0 WHERE id = ?",
	       (500,))
# What do you think is the analogy in Pandas here?
# What if you also want to change multiple rows in Pandas?

input()
print("After the change")
# Let's select everything this time, to make sure only one row was changed.
cursor.execute("SELECT * FROM locations")
after_change = cursor.fetchall()
for row in after_change:
	print("\t%s" % (row,))
print("Only fake station was changed")

# So what's the deal with parameterization?
# Why use it instead of string formatting if you don't have to use executemany?
# Not only is it more convenient, but it's also safer.
# If you use string formatting, but you don't know what the value is,
# then you don't know if it might be an SQL command.
# This might happen if you're taking user input.
# Sure, the value is in quotes, but I could get out of it,
# just with another single quote.
line = input("Please enter a line: ")
command = "SELECT name FROM station_line INNER JOIN locations ON " + \
	  "station_line.id = locations.id AND line = '%s'" % (line)
print("Executing: %s" % (command))
try:
	cursor.execute(command)
except Exception as e:
	print("This error happened because of a coding mistake: %s" % e)
# This just crashes.
# In other SQL libraries, you can do worse:
# end the instruction with a semicolon, and start a new command.
# sqlite3 on Python does not let you do that,
# but it can still break your program, as you can see.
# Sure, you could get out using an exception handler,
# but there will be many more error cases you'll have to handle,
# and, as you will see in the extra credit, there are worse things you can do
# without causing an obvious error.
# Here's how you should do it.
cursor.execute("SELECT name FROM station_line INNER JOIN locations ON " + \
	       "station_line.id = locations.id AND line = ?", (line,));
input()
print("Executed with parameterization:")
line_stations = cursor.fetchall()
for name in line_stations:
	print("\t%s" % (name))
# In the worst case, you get nothing.

# Now we're done.
# No changes this time, so just close.
connection.close()
