import requests

api_key = "720dfad6d262378ab9f9e2a36c11e7eb"

parameters={
    "lat": 51.5085,
    "lon": -0.1257,
    "exclude": "current,minutely,daily", 
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=parameters) # version 3 is pay only, gives 401 error
response.raise_for_status()
hourly_weather = response.json()["hourly"][0:12]  # next 12 hours forecast

weather_ids = [hourly_weather[i]["weather"][0]["id"] for i in range(len(hourly_weather))] # get weather ids for the next 12 hours
if any(id < 700 for id in weather_ids):
    print("bring a raincoat")
else:
    print("all clear")


