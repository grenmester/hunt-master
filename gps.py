from __future__ import division
import math
EARTH_RADIUS = 6371000 # in meters

def distance_between(coord1,coord2):
    """
    Calculated the distance between two tuples of (latitude,longitude) in degrees
    """
    lat1,long1 = coord1
    lat2,long2 = coord2
    delta_lat = math.radians(lat2 - lat1)
    delta_long = math.radians(long2 - long1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + \
        math.cos(lat1) * math.cos(lat2) * \
        math.sin(delta_long/2) * math.sin(delta_long/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return EARTH_RADIUS * c

def within_radius(desired_location,current_location,radius=10):
    """
    Returns whether or not the desired_location is within the radius of current_location
    """
    return distance_between(desired_location,current_location) <= radius
