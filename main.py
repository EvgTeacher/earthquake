import requests
import sqlite3
import random


def save_data(place_magnitude_list):
    conn = sqlite3.connect('data.bd')
    c = conn.cursor()
    # c.execute('CREATE TABLE earthquake (place TEXT, magnitude REAL)')
    c.executemany("INSERT INTO earthquake VALUES(?, ?)", place_magnitude_list)
    conn.commit()
    conn.close()

def result():
    conn = sqlite3.connect('data.bd')
    c = conn.cursor()
    c.execute('SELECT * FROM earthquake')
    data = c.fetchall()
    print(data)
    [print(row) for row in data]
    # for i in data:
    #     print(i)

    conn.commit()
    conn.close()



url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

# start_time = input('Enter the start time')
# end_time = input('Enter the end time')
# latitude = input('Enter the latitude')
# longitude = input('Enter the longitude')
# max_radius_km = input('Enter the max radius in km')
# min_magnitude = input('Enter the min magnitude')

start_time = '2019-01-01'
end_time = '2019-02-01'
latitude = '51.50'
longitude = '-2.0'
max_radius_km = '3000'
min_magnitude = '2'

data_params = {'format': 'geojson', 'starttime': start_time, 'endtime': end_time, 'latitude': latitude,
               'longitude': longitude, 'maxradiuskm': max_radius_km, 'minmagnitude': min_magnitude}
respons = requests.get(url, params=data_params)

data = respons.json()
place_magnitude_list = []
for elem in data["features"]:
    place_magnitude_list.append((elem['properties']['place'], elem['properties']['mag']))

# save_data(place_magnitude_list)
result()
