import csv

from geopy.geocoders import Nominatim
import pandas as pd

file_in = pd.read_csv("lib.csv")

# List of town names
town_names = file_in['Towns']


def write_to_csv(filename: str, data: iter):
    with open(filename, 'a+', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)


# Specify the bounding box for Ghana
# view_box = "1.1496, 11.0985, -4.2715, 3.8826"
view_box = "1.0601216976, 11.0983409693, 4.71046214438, -3.24437008301"  # lat1, lon1, lat2, lon2

# Initialize the Nominatim geocoder with Ghana as the domain
geolocator = Nominatim(user_agent="town-geocoder")
# geolocator = Nominatim(user_agent="town-geocoder", viewbox=view_box)
towns = []
# Loop through the town names and geocode them
for town_name in town_names:
    location = geolocator.geocode({
        'city': town_name,
        'country': 'Liberia',
    })
    if location is not None:
        town = {
            "name": town_name,
            "lat": location.latitude,
            "long": location.longitude
        }
        print(town)
        write_to_csv('liberia_cities.csv', town.values())
        towns.append(town)
    else:
        # write_to_csv('not_found.csv', (town_name, 0, 0))
        print("Location not found for:", town_name)

# for i in towns:
#     print(i)

print(f"\n\nTotal Towns: {len(town_names)}\nFound: {len(towns)}\nNot Found: {len(town_names) - len(towns)}")
