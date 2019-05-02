from math import sin, cos, sqrt, atan2, radians
import geojson


def distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


def meters_to_feet(m):
    f = (m / .3048)
    return f

def get_lat_long_list_from_file(file_name):
    final_list = []
    with open(file_name) as json_file:

        feature_collection = geojson.load(json_file)
        coords = list(geojson.utils.coords(feature_collection))

        for x in coords:
            final_list.append({"lat" : x[1], "long" : x[0]})

        return final_list

