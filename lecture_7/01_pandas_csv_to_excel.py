# Last time I briefly talked about CSV and Excel.
# This time, I'll talk about all the nice things you can do with it
# using some data processing modules.
# Excel had the extra step of choosing a sheet,
# that was not necessary for CSV.
# But if you tried opening the CSV file, you'll only get strings.

INPUT_FILE = "subways.csv"

from csv import reader
csv_file = open(INPUT_FILE, "r")
raw_csv = reader(csv_file)
raw_csv_rows = list(raw_csv)
csv_file.close()
input(repr(raw_csv_rows))

# Fortunately, you can bypass this issue using Pandas.
# It can read a CSV, and convert columns that are all numbers into numbers.
# You just import read_csv, and run it on the file name.
# You'll get something called a DataFrame.
from pandas import read_csv
csv_frame = read_csv(INPUT_FILE)

# You don't even have to worry about the first row.
# It'll figure out those are the column names.
# It then automatically starts counting the indexes from the second row.
input("Columns: %s\nRows: %s" % (csv_frame.columns, csv_frame.index))

# Here's where things get a little unintuitive.
# For the csv module, you get an iterable object of lists,
# and each list is a row.
# So you iterate through rows.
# And if you turn the object into a list,
# when you give an index, you get a row.
# In some respects, DataFrames are kind of like dictionaries,
# where the keys are column names, and the values are the columns.
# So you iterate through the column names.
for column in csv_frame:
	print("Column %s" % (column))
input()
# And when you give a key, you get the column.
input("Column by name: %s" % (csv_frame["NAME"]))
input("That was a column by name")
# You can also give a list of multiple columns.
input("Column by name: %s" % (csv_frame[["OBJECTID", "NAME"]]))
input("That was multiple columns")
# You might complain, because when you input, or get data,
# you probably mostly care about individual rows.
# But pandas does a lot of data processing for you,
# and it works on whole columns at once.
# If you think of a row as an object, each column is a field.
# So working on a column is like working on the same attribute of each row.
# In fact, each column is an attribute.
# This is the same column we saw before.
input("Column as attribute: %s" % (csv_frame.NAME))
input("That was a column by attribute")

# Now which columns might be important in identifying the station?
# That might be more interesting than the row number.
# We can use set_index to set a column to be the index.
# The ID not quite the same as the row number,
# because it skips a bunch of numbers around 470.
# But you will see that most methods don't change the object itself,
# so if you want to keep the changes, you need to overwrite the variable
# with the new value.
csv_frame = csv_frame.set_index(csv_frame.OBJECTID)

# Now here's where things get a little weird.
# If you try to get a slice, DataFrames start acting like lists or tuples.
# The way you can remember this is that for columns,
# there is not usually a natural way to order them.
# But for rows, there is the notion that some rows might have come later.
input("Rows by slices: %s" % (csv_frame[469 : ]))
# Is this the index, or is this the position of the row in the table?

# That said, there is just the incidental order of the columns,
# and you can use loc to
# slice both rows and columns, and get a new DataFrame.
# What's up with this? Let's look at the code.
# This looks a little different,
# even if we ignore just the fact that the rows are smaller.
# This is slicing by name. 470 and 643 are actually the row names;
# We don't have a 643rd row.
# They don't always have to be numbers,
# they just happen to be numbers for spreadsheet rows.
# So there is not necessarily a concept of less than.
# So it's inclusive.
input("Rectangle selection by name: %s" % (csv_frame.loc[470 : 643,
							 "NAME" : "LINE"]))
# You don't have to give continuous slices.
# You can also give lists of the rows and columns you want.
# So here we just pick two rows and two columns, and skip the stuff in between.
input("Pick columns and rows by name: %s" % (csv_frame.loc[[470, 643],
							   ["NAME", "LINE"]]))
# You could use this to get single elements, too.
# But the at field is optimized just for single element access,
# so I recommend you use that.
input("Pick element by names: %s" % (csv_frame.at[2, "NAME"]))
# What happens if you just want to use numbers?
# You could always translate numbers to row indexes and column names.
# I showed you the index and columns fields before.
# Those are like lists.
# So early on, everything gets shifted.
input("Row %d: %s" % (469, csv_frame.index[469]))
# Later, it starts skipping IDs.
input("Row %d: %s" % (472, csv_frame.index[472]))
# More interesting are the columns. It's in the natural order, though.
input("Column %d: %s" % (2, csv_frame.columns[2]))
input("Column %d: %s" % (4, csv_frame.columns[4]))
# But the loc and at methods,
# you can do almost the same things with the numbers,
# just by adding "i" in front of the field name.
# This time it looks more familiar. Row 472 and column 4 are not included,
# so we only have 2 rows and 2 columns.
input("Rectangle selection by column number: %s" % (csv_frame.iloc[469 : 472,
								   2 : 4]))
input("Pick columns and rows by column number: %s" %
      (csv_frame.iloc[[469, 472], [2, 4]]))
input("Pick element by numbers: %s" % (csv_frame.iat[1, 2]))

# Now let's do some processing.
# If you look at the CSV sheet, the location column looks a little inconvenient.
geom_column = csv_frame["the_geom"]
input("Location column: %s" % (geom_column))
# Let's strip of the "POINT (" at the beginning and the ")" at the end.
# The column is a Series object,
# and it has string methods under str.
# Why would you want to use this?
# We can slice it, but we'll have to use the slice method.
stripped_column = geom_column.str.slice(len("POINT ("), -1)
input("Stripped column: %s" % (stripped_column));
# We can also split it. But be careful.
# By default, we would get a Series object,
# where each element is a list of the split strings.
# That makes working with each one a little hard.
# So let's make that into a DataFrame, by setting the expand parameter to True
geom_frame = stripped_column.str.split(" ", expand = True)
input("Split columns: %s" % (geom_frame))
# Now we can get separate series. This time, the column names are numbers.
longitude = geom_frame[0]
latitude = geom_frame[1]
input("Longitude: %s" % (longitude))
input("Latitude: %s" % (latitude))

# We got Series of objects. But we want numbers.
# Toget that, use the to_numeric function from pandas.
from pandas import to_numeric
longitude_numbers = to_numeric(longitude)
latitude_numbers = to_numeric(latitude)
input("Longitude: %s" % (longitude_numbers))
input("Latitude: %s" % (latitude_numbers))

# Now let's assemble our own DataFrames
# Let's create one where we just have the locations.
# We already have the two columns.
# As I said, DataFrames can be accessed like dictionaries.
# And you can also construct a DataFrame with a dictionary,
# where the keys are column names, which we make up,
# and the values are the columns that we already have.
# To make it easier to look things up, let's also include the names and IDs.
# We can also set the index explicitly to the object id.
# It's not required. Either it automatically creates them from 0,
# or tries to guess based on the indexes of one of the columns
# that we give it, like the ones from csv_frame.
from pandas import DataFrame
locations = DataFrame({"id": csv_frame["OBJECTID"],
		       "name": csv_frame["NAME"],
		       "longitude": longitude_numbers,
		       "latitude": latitude_numbers},
		      index = csv_frame["OBJECTID"])
input("Locations frame: %s" % (locations))

# Let's create another DataFrame. This will take more direct changes.
# Notice how the last DataFrame printed out the columns in a different order
# than we gave it. That's because we used dictionaries.
# Let's try a sorted set of columns.
# Only include the station ID and line,
# because the names are actually not unique.
STATION_LINE_COLUMNS = ["id", "line"]
# Let's start with empty columns, and we'll fill them in later.
station_line = DataFrame(columns = STATION_LINE_COLUMNS)
# This time we want to a DataFrame where each row
# is a pair between a station and its line.
# What's wrong with just having a list of lines for each station?
# All the tools we use today will be working on individual columns,
# which are fixed ahead of time, because each column has a special meaning.
# By using pairs, we only need two columns.
# We want to get the lines for each station.
# We already have that in the old DataFrame, but we need to split the lines.
# If we just took it out and split it, we'd lose a lot of context.
# So let's just change it.
# With the same indexing methods I mentioned previously,
# you can also change cells and columns.
# Let's change the LINE column.
# This time, we don't know how many columns there might be ahead of time,
# so we can use the default split.
old_line = csv_frame["LINE"]
# If you look at the CSV file, there is a dash between each line.
split_line = old_line.str.split("-")
input("Separate lines: %s" % (split_line))
# Now let's replace the column.
csv_frame["LINE"] = split_line
# Now you can iterate through the rows, using the itertuples method.
# We'll need to create Series for rows.
from pandas import Series
for row in csv_frame.itertuples():
	# You can turn it into an ordered tuple, using the tuple constructor,
	# but it's more like an object,
	# where each column is a public field.
	object_id = row.OBJECTID
	lines = row.LINE
	# If you just wanted a tuple of the whole thing,
	# you could have just written tuple(row)
	# And just as you append to a list,
	# you append rows to a DataFrame, because it's like a list of rows.
	for line in lines:
		# Here is the row, with the columns labeled.
		row = Series([object_id, line], index = STATION_LINE_COLUMNS)
		# There are two caveats with append.
		# First, it wants an index by default.
		# Let the DataFrame automatically create the indexes.
		# Secondly: append does not actually change the DataFrame,
		# so we have to assign the result to the old variable.
		station_line = station_line.append(row, ignore_index = True)

input("Stations and lines: %s" % (station_line))

# Now we can write all this out to a file.
# We could write the new DataFrames to two separate CSV files,
# using to_csv.
locations.to_csv("locations.csv")
station_line.to_csv("station_line.csv")
# If you open them up, you see the columns, as they appear in the DataFrames.
# You also see the row indexes and column names.

# We could also write both of them as separate sheets on an Excel file.
# To write twice to the same excel sheet without changing it,
# instead of giving a name, give an ExcelWrite object
# that keeps track of all changes for you.
from pandas import ExcelWriter
excel_writer = ExcelWriter("stations.xlsx")
# Write using to_excel, giving it the writer object, and the sheet name.
locations.to_excel(excel_writer, "locations")
station_line.to_excel(excel_writer, "station_line")
# Don't forget to save.
excel_writer.save()
