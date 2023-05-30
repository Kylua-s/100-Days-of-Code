# Exercise 35 - CSV
# Extract the temp data from a csv files

import csv

with open("weather_data.csv") as weater_file:
    data = csv.reader(weater_file)
    next(data, None)
    temperature = []
    for row in data:
        temperature.append(int(row[1]))

print(temperature)
