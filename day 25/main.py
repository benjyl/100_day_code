import os
import csv

path = os.getcwd()
print(path)

with open(path+"\\day 25\\weather_data.csv") as file:
    # data = file.read().splitlines()
    data = csv.reader(file)
    temps = []
    for row in data:
        if row[1].isnumeric():
            temps.append(row[1])
        
print(temps)
# print(data)