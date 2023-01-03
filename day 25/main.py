import os
import csv
import pandas

path = os.getcwd()
data =pandas.read_csv(path+"\\day 25\\weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temps = data["temp"]

# list mean
temp_list = data["temp"].to_list()
mean_temp = sum(temp_list)/len(temp_list)
print(mean_temp)

# pandas mean
print(temps.mean())
#max 
max_temp = temps.max()
# print row with max temp, condition
print(data[data.temp == max_temp])

#monday temp
monday_temp = int(data[data.day == "Monday"].temp)
monday_temp_fahr = monday_temp*1.8 + 32
print(monday_temp_fahr)

#create dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Benjy"],
    "scores": [95, 83, 90]
}

student_dataframe = pandas.DataFrame(data_dict)
student_dataframe.to_csv("test_data.csv")
print(student_dataframe)