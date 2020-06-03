# Now let's try to get the data from Excel.
# Analogously to read_csv, you use the function read_excel,
from pandas import read_excel

BOOK_NAME = "stations.xlsx"
# But, again, you have to give the sheet name.
locations = read_excel(BOOK_NAME, "locations")
station_line = read_excel(BOOK_NAME, "station_line")

print("locations sheet:\n%s" % (locations))
input("that was locations")
# Rather annoyingly, they don't treat the first column as the index.
# They just go by the row number, minus 2.
# Why do you think that is?
# Anyways, we can drop that extra column.
# We need to set the axis parameter to 1, to say we're dropping a column,
# not a row, which is 0.
locations = locations.drop("OBJECTID", axis = 1)
# Now let's set the index right again
locations = locations.set_index(locations.id)
print("station_line sheet:\n%s" % (station_line))
input("that was station_line")

# Now let's do some more processing.
# pandas is actually based on numpy,
# which makes it faster and easier
# to process a bunch of numbers at the same time.
# We have latitude and longitude.
# You can use that to calculate the distance between two location.
# In the last lecture's notes, I included a module
# for calculating that. But that one is only for two coordinates.
# This time, we can find the distance between multiple coordinates.
# A lot of the arithmetic functions are overwritten by numpy,
# so that you can apply the same operation on everything inside a Series.
# There are some more complex, but common math functions
# that numpy also supports.

# First, we'll need the basic constant, pi
from math import pi
# But the rest of the functions, we don't import from math.
# Instead, we import them from numpy.
from numpy import arcsin, sin, cos

# We also need the approximate radius of the earth:
# https://en.wikipedia.org/wiki/Earth_radius
EARTH_RADIUS = 6371.0

# The formulas here work on angle, in radians.
# angle is actually a Series.
def haversine(angle):
	"""haversine(angle) -> haversine of x
	angle: angle, in radians"""
	# If you do an operation with a Series
	# and a single value, also called a scalar,
	# you apply the same operation, with the same constant,
	# with every element in the series
	half_angle = angle / 2
	# numpy.sin is applied on each element.
	half_sine = sin(half_angle)
	# If you do operations between two Series or two DataFrames,
	# you get the result of the operation done between
	# corresponding elements.
	# This is different from normal math,
	# where vector and matrix multiplications mean different things.
	return half_sine * half_sine

# But locations are usually in degrees.
# We just apply a bunch of operation involving scalars on the whole Series.
# What if we give it a scalar, though?
def deg_to_rad(deg):
	"""haversine(deg) -> rad
	deg: angle in degrees
	rad: angle in radians"""
	return pi * deg / 180.0

# Calculate the distance between two points,
# given their latitude and longitude using the
# haversine formula: https://en.wikipedia.org/wiki/Haversine_formula
def earth_dist(lat_0, long_0, lat_1, long_1):
	"""earth_dist(lat_0, long_0, lat_2, long_1) -> distance
	lat_0: the latitude of the first point, in degrees
	long_0: the longitude of the first point, in degrees
	lat_1: the latitude of the second point, in degrees
	long_1: the longitude of the second point, in degrees
	distance: the distance between the two points, in kilometers"""
	# Convert the angles
	lat_0_rad, long_0_rad, lat_1_rad, long_1_rad = \
	map(deg_to_rad, (lat_0, long_0, lat_1, long_1))

	# Why does this work?
	right_hand_side = haversine(lat_1_rad - lat_0_rad) + \
			  cos(lat_0_rad) * cos(lat_1_rad) * \
			  haversine(long_1_rad - long_0_rad)
	asin_res = arcsin(right_hand_side ** 0.5)
	return 2 * EARTH_RADIUS * asin_res

# Now, let's ask the user for the location, which will be our scalars.
# Check if we get real numbers.
# Let's try the Math building, whose coordinates are 40.8091087, -73.9648563
latitude = 40.8091087
longitude = -73.9648563

dists = earth_dist(locations.latitude, locations.longitude, latitude, longitude)
# Let's put this in the DataFrame with the locations.
locations["distance"] = dists
# We can sort it all together, by one of the columns,
# using sort_values, and the by parameter gives us the column
sorted_stations = locations.sort_values(by = "distance")
input("Sorted by distance:\n%s" % (sorted_stations))

# What else can we do?
# We can select by some criteria.
# Say we only want stations that are within 1 kilometer.
close_stations = sorted_stations[sorted_stations.distance < 1.0]
input("Stations within 1 kilometer:\n%s" % (close_stations))

# What just happened? How does it do that?
# That's the nice thing about overriding operators.
# pandas not overrode both the comparison operator,
# so we get a table of truth values:
print("Is the station within 1 kilometer?:\n%s" %
      (sorted_stations.distance < 1.0))
input("Comparison gave us a truth table.")
# And the indexing operator also accepts the truth table,
# and filters out any false entries.

# We can also pair the stations with their respective lines.
# We can use the merge method.
# We create a new DataFrame that combines rows from
# both old DataFrames, that have the common key, specified by the on keyword.
inner_joined = close_stations.merge(station_line, on = "id")
input("inner join:\n%s" % (inner_joined))
# We got lucky here, because the column we want to join on had the same name.
# What if it's not?
# We can try renaming one of the sheets' columns.
# Use the rename method, and the columns parameter,
# and a dictionary to say what we want to rename.
# We want to rename "id" to "object_id", so the key is "id",
# and the value is "object_id".
# Again, we don't actually change anything, but we get a new object.
renamed_close = close_stations.rename(columns = {"id": "object_id"})
input("Renamed columns:\n%s" % (renamed_close.columns))
# This time we have to name the ID's separately,
# left_on refers to the key in the DataFrame whose method we're using,
# which is renamed_close.
# right_on refers to the key in the DataFrame in the method parameters,
# which is station_line.
inner_joined = renamed_close.merge(station_line, left_on = "object_id",
				   right_on = "id")
input("inner join with different keys:\n%s" % (inner_joined))
# A little uglier with the extra column.
# But we can remove that with drop, again.
inner_joined = inner_joined.drop("object_id", axis = 1)
input("inner join with same column removed:\n%s" % (inner_joined))

# We also got lucky because for every station,
# there is at least one line.
# Let's make up one that is right where we are, but has no lines.
from pandas import Series
extended_close = close_stations.append(Series([500, latitude, longitude,
					       "fake", 0.0],
					      index = ["id", "latitude",
						       "longitude", "name",
						       "distance"]),
				       ignore_index = True)
input("With fake station:\n%s" % (extended_close))
inner_joined = extended_close.merge(station_line, on = "id")
input("inner join with fake station:\n%s" % (inner_joined))
# This is what is called an inner join.
# It only counts rows if both DataFrames have a shared key.
# There is something called outer join, which, in its full form,
# combines rows from both DataFrames,
# including those that cannot be paired.
# You still see some pairs, but also some with no match.
# That's because every station and station-line pair must appear at least once.
outer_joined = extended_close.merge(station_line, on = "id", how = "outer")
print("outer join:\n%s" % (outer_joined))
input("that was an outer join")
# There are more specific forms.
# left outer join keeps all rows from the DataFrame whose merge method we call,
# and only keeps the rows of the DataFrame in the parameter,
# if the key matches that of one in the first frame.
# You set the how parameter to "left".
# This time, you'll see the fake station.
left_joined = extended_close.merge(station_line, on = "id", how = "left")
print("left join:\n%s" % (left_joined))
input("that was a left join")
# Right join does the reverse. You set how to "right".
# This time, you'll see all of the pairs, even if there is no station.
# But you won't see the fake station.
right_joined = extended_close.merge(station_line, on = "id", how = "right")
print("right join:\n%s" % (right_joined))
input("that was a right join")

# Now you're seeing a lot of thing's called "NaN",
# which shows up for columns for which the corresponding
# DataFrame does not have key.
# That's numpy's version of None.
# It also shows up if you do something that would normally lead to a crash,
# say you divide one Series by another Series that has 0.
# If you used it in calculation, it would make the result also NaN,
# but a lot of panda's functions and method let you ignore it.
# If you want to remove rows with NaN in a DataFrame,
# just call the dropna method.
# Again, it doesn't change the original object.
no_nan = left_joined.dropna()
input("left join without NaN:\n%s" % (no_nan))
# Same result as the first inner join.

# We don't get anything new.
# So how about we keep the NaNs, and replace them with something?
# You use the fillna method, and replace the NaNs with 0.
nan_0 = left_joined.fillna(0)
print("left join with NaN filled with 0:\n%s" % (nan_0))
input("NaNs are filled with 0")

# Why would you ever want to use join?
# It lets you combine separate, but related DataFrames,
# so you can analyze a single object with more columns.
# For example, say we want to find all of the closest stations,
# but only those on the A line.
# We need to know both the distance and line.
# The inner join combines them. What does this do?
closest_a = inner_joined[inner_joined.line == "A"]
input("closest stations on A line:\n%s" % (closest_a))

# Pandas helps you a lot with getting aggregate information.
# Like get the statistics, using the describe method, both on a column:
input("Statistics on distances:\n%s" % (sorted_stations.distance.describe()))
# And a whole DataFrame. Of course, not everything is useful.
input("Statistics on all columns:\n%s" % (sorted_stations.describe()))
# This is convenient not only because it goes through the whole DataFrame,
# but also because it ignores any NaN.

# But that's really broad,
# and then there's the fact that when you do merging,
# you might get a lot of repeated values.
# How about you want to get the average distance or average location per line?
# What data does this have? What could repeat?
location_line = locations.merge(station_line, on = "id")
# You can group together rows with the same subway line,
# using the groupby method.
grouped_by_line = location_line.groupby("line")
# Now you can do many things, like find the maximum
# of all of each group of cells. All of these, like describe, ignore NaN.
print("Maximum by line:\n%s" % (grouped_by_line.max()))
input("Those were maxima")
# What is happening? We grouped by line.
# But we did not group by name, id, location and distance.
# So the rows that have the same line are in the same group,
# and we are getting the maximum of each group, per column.
print("Minimum by line:\n%s" % (grouped_by_line.min()))
input("Those were minima")
# Or the minimum.
print("Average by line:\n%s" % (grouped_by_line.mean()))
input("Those were averages")
# Or the average.
# Where else could this be useful?
# For example, you want to know the average temperature of cities of each state.
# You could have many cities in the same state,
# so the state will repeat. So you group by state,
# and then you calculate the average.
# Which column will have the average temperature?

# You have all these DataFrames,
# and you're probably getting tired of just reading them.
# Let's plot them.
# pandas uses matplotlib, and there are some matplotlib
# functions and objects we'll need.
# But pandas Series and DataFrames have methods for being plotted directly.
# For example, let's plot the object ID column.
# That becomes the y axis. We'll figure out what the x axis is.
locations.id.plot()
# We still have to tell matplotlib to show it,
# and also set the title and labels.
# Make sure to set the title and labels only after you have a new plot.
# Otherwise, pyplot won't know where to put the text.
from matplotlib.pyplot import show, title, xlabel, ylabel, close
# title sets the plot title.
title("Object IDs")
# xlabel sets the label for the x axis
xlabel("Mysterious X axis")
# ylabel sets the label for the y axis
ylabel("Object ID")
show()
# What's the x axis? It's the row index.
# If I didn't set the title, it would automatically label it as such.
# Also note that there is no gap where there are no stations.
# They interpolate gaps.
# That means if there are missing indexes,
# surrounded by indexes with data,
# Panda will try to guess.
# It does not extrapolate --it does not make up points outside
# of the range of known indexes.

# The code also needs to close the figure.
# Just closing the window won't work.
# Python will still keep data in the background, and that can add up.
close()
# You can look around, and even save the plot.

# You can also plot all columns in a DataFrame.
# Each part is a different column.
# Doesn't make too much sense if each column is something different,
# but it's still possible.
locations.plot()
title("All the columns")
# The x axis is automatically labelled by the name of the index.
# This time there is no real-life meaning for the Y-axis
ylabel("Y-Axis")
show()

# It might make sense to plot each column in a separate plot.
# But you can still do that all at once.
# Just set the subplots parameter to True.
locations.plot(subplots = True)
# You see that the x and y values of each point are exactly the same.
# Why is that? Because the x axis is actually the index,
# which also happens to be the object ID.
show()

# It probably makes more sense to plot each line separately.
# Say we want to visualize which line goes through each station.
# We want the X axis to be the station ID,
# and each value on the Y axis represents a line.
# Now, the number would not be very useful,
# but it would be clear which line it was,
# if we plotted each line separately.
# Let's create a new column, where we have a numerical value for each line.
# First, we need to create a table mapping line to number.
# In regular Python, how would you do that while making sure
# you don't repeat any lines?
# But here, we already have a DataFrame that we grouped by lines,
# so each group is a line name.
line_lookup = {}
for line in grouped_by_line.groups:
	line_lookup[line] = len(line_lookup) + 1
# Now how would you actually do the conversion in Python?
# For pandas, you can use the apply method on a Series, like a column.
# That's the only new thing we've done so far.
converted_line = location_line.line.apply(lambda line: line_lookup[line])
# And just set the column. This is review, again.
location_line["line_number"] = converted_line
# Now here's the big question: When you plot a DataFrame,
# it plots all columns separately.
# But the data you want is in one column.
# How do you split that?
# Using the pivot_table function.
from pandas import pivot_table
# It lets you choose one particular column,
# and then split it among different columns, say the line number,
# which are determined by the data from other columns, say the line name.
# You can also set the columns --yes, that's multiple columns--
# that you want to use as the new index.
# You have to give it the DataFrame.
# values is the column whose values you want to split up.
# columns is the list of columns whose data form new columns,
# in which the values are put.
pivoted = pivot_table(location_line, values = "line_number", \
		      columns = ["line"], index = ["id"])
print("Pivoted:\n%s" % (pivoted))
input("pivoted table")
# So there are 473 rows. That happens to be the number of stations.
# But didn't the inner join repeat the same station for many lines?
# The nice thing is that the index parameter kind of has an effect like groupby.
# It will aggregate all of the old rows that have the same, designated index.
# By default it "aggregates" by taking the average, while ignoring any NaNs.
# So if you only have one value for the cell, that's the value it'll take.
# Speaking of NaNs, there sure are a lot of them,
# but we don't have to worry during plotting,
# because
# Now, let's plot that.
pivoted.plot()
title("Lines as lines")
# The x axis is the index, and is labeled so.
ylabel("Line number")
show()
# In the background, the gaps are actually represented as NaN.
# Why doesn't it interpolate?
# The data is not missing. The indexes are there, but as NaN.
# NaN is just not plotted.
# Notice that there is a huge gap, because not all station ID's are taken.
# Interpolation doesn't happen there, either. Why?
# Look at the stations around the gap.

# We could also make a scatter plot of some chosen lines.
# What data does this have?
data_a = location_line[location_line.line == "A"]
data_1 = location_line[location_line.line == "1"]
# Say, why does this work?
data_2 = location_line[station_line.line == "2"]

# This time we want to put multiple scatter plots from separate DataFrames.
# We create the plot. We also tell it how to color and label it.
# The "ax" you see. That is the place where the plot is put.
# It lets you reuse the same area,
# and also, when you have multiple areas, you get to choose one.
ax = data_a.plot.scatter(x = "longitude", y = "latitude",
			 color = "Blue", label = "A")
# And tell the second DataFrame to plot on it, too.
data_1.plot.scatter(x = "longitude", y = "latitude", ax = ax,
		    color = "Red", label = "1")
title("Stations of lines A and 1")
show()

# We can do a little bit more with scatter plots.
# We can also add a third dimension with those dots.
# Let's say we don't only care about stations,
# but also how many lines run through them.
# We have the same station maybe repeated many times, with different lines.
# We need to group them by their station. Let's use groupby again.
grouped_by_station = station_line.groupby("id")
# This time, we don't actually have numbers,
# so the statistics we got before don't make much sense.
# But we can still get the count of the cells that are not NaN.
line_count = grouped_by_station.count()
print("Lines through each station:\n%s" % (line_count))
input("Counted lines going through each station")
# The columns are all the same because there is no NaN.
# So we can pick an arbitrary column to get the count.
# We also need the location. So we merge with the location table once more.
# This time, because of what we grouped by, the right DataFrame
# has the ID as its index.
# So we have to say that we want to use the right DataFrame's index
# for merging, using right_index.
# Because we set the index to be the station ID, the locations DataFrame
# using left_index has the same effect for locations.
# So let's use them both.
# We don't have to, though; we could also use left_on,
# because we have an ID column.
location_line_count = locations.merge(line_count, left_index = True,
				      right_index = True)
input("Lines through each station with location:\n%s" % (location_line_count))
# This time, there is a third dimension, the number of lines,
# which we use for the color of the dot, using the "c" parameter.
# Let's make the dots a little bigger with the "s" parameter.
location_line_count.plot.scatter(x = "longitude", y = "latitude", c = "line",
				 s = 50)
title("Stations and number of lines")
# We can add more stuff on a plot, though. We could add labels inside it.
from matplotlib.pyplot import text, annotate
# text just adds a text label inside your plot.
# You just enter the coordinates where you want the text, and the text.
text(longitude, latitude, "CU Math")
# annotate gives you an arrow, you give the xy parameter as a tuple,
# to say where it points to,
# and xytext, also as a tuple, to say where the text should be.
# You'll also need arrowprops, if you want an arrow.
# Let's give it a width of 1.
annotate("We are here", xy = (longitude, latitude),
	 xytext = (longitude - 0.05, latitude + 0.05),
	 arrowprops = {"width": 1})
show()

# There is an easier way to get the count, though.
# If we don't already have the grouped information,
# we could take the line column,
# and take the count of each value.
# Which way you want to use depends on whether you already did the grouping.
print("Counted lines going through each station, the easy way:\n%s" %
      (station_line.id.value_counts()))
input("Counted lines going through each station the easy way")
# This time, it's sorted by count, from highest to lowest.
# So we know that station number 15 has the most lines. That's DeKalb Avenue.

# Now a final thing on plotting.
# We have so many things we can plot.
# Let's plot them all together in one figure,
# kind of like how we did it with subplots = True
# for the different columns in one DataFrame,
# but we can do it with multiple DataFrames,
# in a very controlled way.
# You use subplots, which allocates a set of axes,
# which are just the places where you put a plot.
from matplotlib.pyplot import subplots
# The first parameter is the number of rows,
# and the second is the number of columns.
# Say we want to create 3 plots, all in one row.
# We get a figure object, and a list of axes.
fig, axes = subplots(1, 3)
# This time you tell plot to plot on the particular axis, as they call it.
locations.id.plot(ax = axes[0])
# This time, to set the title and axes,
# you use the ax's method whose name starts with "set_",
# followed by the name of the function you've been using.
axes[0].set_title("ax 0")
axes[0].set_xlabel("Row Index")
axes[0].set_ylabel("Object ID")

locations.plot(ax = axes[1])
axes[1].set_title("ax 1")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Y-Axis")

pivoted.plot(ax = axes[2])
axes[2].set_title("ax 2")
axes[2].set_xlabel("Station ID")
axes[2].set_ylabel("Line")

# This time we tell the figure object to show.
# Notice that we made it past. So it doesn't actually block this time.
fig.show()
input("We already made it past the show. Press enter to go to closing code.")
# You can pass the figure into the close function this time.
close(fig)
# And this time it disappeared without me clicking the close button.

# Let's try again, this time arranging the subplots vertically
fig, axes = subplots(3, 1)
locations.id.plot(ax = axes[0])
axes[0].set_title("ax 0")
axes[0].set_xlabel("Row Index")
axes[0].set_ylabel("Object ID")

locations.plot(ax = axes[1])
axes[1].set_title("ax 1")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Y-Axis")

pivoted.plot(ax = axes[2])
axes[2].set_title("ax 2")
axes[2].set_xlabel("Station ID")
axes[2].set_ylabel("Line")

# This time we tell the figure object to show.
# Notice that we made it past. So it doesn't actually block this time.
fig.show()
input("Subplots arranged vertically.")
# You can pass the figure into the close function this time.
close(fig)

# But if you have multiple rows and columns,
# what does that look like?
# Let's say we want to make four plots in a 2-by-2 grid.
fig, axes = subplots(2, 2)
# This time you have to specify both grid coordinates.
# This is the upper left corner. That's where you start.
locations.id.plot(ax = axes[0][0])
axes[0][0].set_title("ax 0, 0")
axes[0][0].set_xlabel("Row Index")
axes[0][0].set_ylabel("Object ID")

# This is the upper right corner. The second coordinate is the column.
locations.plot(ax = axes[0][1])
axes[0][1].set_title("ax 0, 1")
axes[0][1].set_xlabel("Index")
axes[0][1].set_ylabel("Y-Axis")

# This is the lower left corner. The first coordinate is the row,
# and you go down for the next row.
pivoted.plot(ax = axes[1][0])
axes[1][0].set_title("ax 1, 0")
axes[1][0].set_xlabel("Station ID")
axes[1][0].set_ylabel("Line")

# We can also make a scatter plot.
# plot is just a generalization of many kinds of plots.
# Where do you think this one goes?
location_line_count.plot.scatter(x = "longitude", y = "latitude", c = "line",
				 s = 50, ax = axes[1][1])
# And, turns out annotate and text are just methods of the axis.
axes[1][1].text(longitude, latitude, "CU Math")
axes[1][1].annotate("We are here", xy = (longitude, latitude),
		    xytext = (longitude - 0.05, latitude + 0.05),
		    arrowprops = {"width": 1})
axes[1][1].set_title("ax 1, 1")

# Now that we have the axes, if you want to,
# matplotlib lets you draw graphs on them,
# using none other than a method called plot,
# and other specific plotting methods.
# pandas and matplotlib both use numpy,
# which contains what is called an array which is like a list,
# so that you can operate on a bunch of numbers all at once.
# There are two similar concepts you have seen before in Python itself.
# What are they?
# Usually Pandas will give you all the data you need,
# but sometimes you want to generate points yourself,
# say using a mathematical function.
# So all you need are the x values and the function. Why?
# What do you do if you want a regularly spaced sequences of numbers?
from numpy import arange
# numpy lets you get a sequence of numbers, like a range,
# except with an arbitrary step, that could be a floating point number.
# And it happens to be a numpy array, which is what arange stands for.
# So let's try this linear function for the first plot.
x = arange(0, 700, 0.1)
# Let's plot lines below and above the point.
# You can plot any set of coordinates using the plot method of the axis.
# You just give triplets of the x values, the y values, and the style.
# Here, "r" and "k" mean red and black. - means a solid line.
axes[0][0].plot(x, x - 5, "r-", x, x + 5, "k-")
# Let's also show some more space before and after the indexes with data,
# to prove that Pandas does not extrapolate.
# Use the axis method.
axes[0][0].axis([-100, 800, -100, 800])

# This time we tell the figure object to show.
# Notice that we made it past. So it doesn't actually block this time.
fig.show()
input("Subplots arranged with multiple rows and columns.")
# You can pass the figure into the close function this time.
close(fig)

# Now before we leave Pandas, let's put the data we read into a sqlite database.
# There are many implementations of what are called relational databases.
# Most of them use a variation of a language called SQL.
# I'm not going to teach you all of SQL in one lecture.
# But there are concepts in relational databases
# that I have already shown in Pandas,
# and I'll show you their analog in sqlite.
# Relational databases are called that because
# they have tables with fixed rows,
# and each row shows a relationship between the values of the cells
# in each column. This is exactly how Pandas works.
# So it's quite easy putting all of this data into a database.
# Most SQL-based databases connect to "talk" to an external database.
# For sqlite, you connect using the function sqlite.connect
from sqlite3 import connect
# Just a small caveat, if you're using Pandas or Numpy,
# and then want to write data to SQL.
# They have their own number types.
# So you have to call register_adapter from sqlite to convert the numbers.
# These are the types from Numpy.
from numpy import int64, float64
# The register_adapter function lets you convert any instance of a type
# using a function you give it.
from sqlite3 import register_adapter
# Remember that constructors are also functions.
register_adapter(int64, int)
register_adapter(float64, float)
# It really just "talks" with a file.
connection = connect("subways.db")
# You get a cursor that you use to get and set data.
# Think of the database as a text file,
# and the cursor lets you browse through it, and make changes.
cursor = connection.cursor()

# We don't have a table yet, so let's create it.
# All commands are run through the cursor,
# using a method whose name starts with execute.
# To create a table, you enter "CREATE TABLE", then the name,
# and then in parentheses, the columns.
# You have the column name, the type.
# We have INT for int, TEXT for string, and REAL for float.
# You can also make one of them the primary key,
# which you use to look up the row. It needs to be unique.
# We can also say which rows cannot be NULL.
# That's SQL's way of saying None.
cursor.execute("CREATE TABLE locations (id INT PRIMARY KEY NOT NULL, " +
					"name TEXT, " +
					"latitude REAL, " +
					"longitude REAL)")
# Now, let's add elements. For good measure, let's also add some fake ones.
# Here, you want to use what are called paramerization.
# It kind of looks like string formatting, but it's more than that.
# For one, if you have a collection, you can execute the same command
# on all elements in the collection.
# You use executemany.
# To insert something into a table, you start with "INSERT INTO",
# and then the name, and then the columns you want to set.
# Then the values, which has a question mark for every element.
# Then you have a collection of tuples which gives you the value
# you want to put in each question mark.
# We add the real rows with a list comprehension,
# and a fake in a separate list.
# Why do I use list comprehension?
cursor.executemany("INSERT INTO " +
		   "locations(id, name, latitude, longitude) " +
		   "VALUES(?, ?, ?, ?)",
		   [(r.id, r.name, r.latitude, r.longitude)
		    for r in locations.itertuples()] +
		   [("500", "fake", latitude, longitude)])

# Let's repeat the same thing with the station_line sheet.
# Why isn't id a key this time?
cursor.execute("CREATE TABLE station_line(id INT, line TEXT)")

cursor.executemany("INSERT INTO station_line(id, line) " +
		   "VALUES(?, ?)", [(r.id, r.line)
				    for r in station_line.itertuples()])

# Don't forget to save again. Use the commit method.
connection.commit()
# Then close the connection.
connection.close()

# Just a few words of caution. Accessing databases is not like accessing files.
# You won't automatically remove all the old data.
# That also means that if you try to create the table again,
# you'll get an error.
# So for your homework, when you're testing,
# make sure to remove the database file each time.
