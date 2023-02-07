import requests
from datetime import datetime

# #response codes
# # e.g. 404 - doesn't exist
# #1XX: Hold on
# #2XX: successful
# #3XX: No permission to access
# #4XX: You mucked up
# #5XX: Server mucked up e.g. server down
# response = requests.get(url="http://api.open-notify.org/iss-now.json") #gets a response code for iss position
# response.raise_for_status() # raises exception and explains error for response
# # get data from response
# data = response.json()
# print(data)

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  # hour of sunrise
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]  # hour of sunset


time_now = datetime.now()
print(time_now.hour)
