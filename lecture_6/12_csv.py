#12_csv

# Not everything you find online is JSON or HTML.
# A lot of data might be stored in spreadsheets.
# There are many different forms. You've probably heard of Excel.
# The simplest form is csv, or comma-separated values.
# It's called that because, in general, these files contain lines,
# each of which is a list of values, usually separated by commas.
# Can't we just parse each line, and split by commas?
# No; what if you have commas in a cell?
# For example, the notes in this CSV file on subway stations in New York,
# from https://data.cityofnewyork.us/api/views/kk4q-3rt2/rows.csv?accessType=DOWNLOAD.
# Let the csv module help you with that.

from csv import reader

# We open the file, and pass it into the reader,
# and we just pass it into the reader function.
csv_file = open("subways.csv", "r")
csv_data = reader(csv_file)

# What can we do with the object?
print("CSV object contains %s" % dir(csv_data))
# It's iterable. Let's turn it into a list.
csv_list = list(csv_data)

# Close the file, just to be safe.
csv_file.close()

# What can we do with that?

# Let's say we want to find the nearest subway station,
# based on our coordinates.
# If you look back at the spreadsheet,
# the third column is the name, and the fourth is the coordinates.

# So let's get them.  The list actually contains lists, one for each row.
name_locations = {}
# Let's skip the header, and go to the data.
# If we iterate over this list, we get lists representing the rows.
for row in csv_list[1 : ]:
	name = row[2]
	point = row[3]
	# But the location is in a weird form, so let's remove that.
	# "Point (" is 7 characters, and we remove the closing parenthesis.
	location_str = point[7 : -1]
	# We split the longitude and latitude, and turn them into real numbers.
	location = map(float, location_str.split(" "))
	name_locations[name] = location

# Now, let's ask the user for the location. Check if we get real numbers.
latitude = None
while latitude is None:
	latitude_str = input("Please enter the latitude: ")
	try:
		latitude = float(latitude_str)
	except ValueError:
		print("%s is not a real number" % latitude_str)
longitude = None
while longitude is None:
	longitude_str = input("Please enter the longitude: ")
	try:
		longitude = float(longitude_str)
	except ValueError:
		print("%s is not a real number" % longitude_str)

# I included a module for calculating the distance.
# Let's use that for finding the shortest station.
from distance import earth_dist
# We look for the closest station
# by looking for the one with the smallest distance
# While we're at it,
# let's also keep track of all of the locations and distances.
min_dist = None
closest_station = None
closest_location = None
by_distance = []
for (name, (station_longitude, station_latitude)) in name_locations.items():
	dist = earth_dist(latitude, longitude, \
			  station_latitude, station_longitude)
	# We pick the next station that beats the last best station,
	# or just pick it if there was no station before.
	if min_dist is None or dist < min_dist:
		min_dist = dist
		closest_station = name
		closest_location = (station_longitude, station_latitude)
	# Let's save the station by distance, name, longitude, and latitude
	by_distance.append([dist, name, station_latitude, station_longitude])

print("The closest station is %s, at (%f, %f), %f kilometres away" %
      (closest_station, closest_location[1], closest_location[0], min_dist))

# Now we got all of the station distances.
# How can we output it? As a CSV.
# Let's sort it by distance, which is easy,
# because each added list in by_distance has the distance first.
by_distance.sort()
# What do we use to write the CSV file?
# We used csv.reader, now we use csv.writer
from csv import writer
csv_out_file = open("distances.csv", "w")
csv_out_data = writer(csv_out_file)
print("writer has attributes %s" % (dir(csv_out_data)))

# We write the rows. Write a single row with writerow. We want the header first.
csv_out_data.writerow(["distance", "name", "latitude", "longitude"])
# Use writerows to write a collection of rows all at once.
csv_out_data.writerows(by_distance)
# Now close.
csv_out_file.close()
