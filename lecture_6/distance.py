from math import pi, asin, sin, cos

# The approximate radius of the earth:
# https://en.wikipedia.org/wiki/Earth_radius
EARTH_RADIUS = 6371.0

def haversine(angle):
	"""haversine(angle) -> haversine of x
	angle: angle, in radians"""
	return sin(angle / 2) ** 2

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
	lat_0_rad, long_0_rad, lat_1_rad, long_1_rad = \
	map(deg_to_rad, (lat_0, long_0, lat_1, long_1))

	right_hand_side = haversine(lat_1_rad - lat_0_rad) + \
			  cos(lat_0_rad) * cos(lat_1_rad) * \
			  haversine(long_1_rad - long_0_rad)
	asin_res = asin(right_hand_side ** 0.5)
	return 2 * EARTH_RADIUS * asin_res
