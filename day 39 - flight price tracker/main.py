# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_searcher = FlightSearch()
sheet_data = data_manager.get_sheet_data(testing=True)
flight_data = FlightData()
notifications = NotificationManager()

print(sheet_data)

add_iata = False  # checks if IATA needs to be added to sheet data
if sheet_data:
    for city in sheet_data:
        print(city)
        if city["iataCode"] == "":
            add_iata = True
            iata_code = flight_searcher.get_IATA_code(city["city"])
            city["iataCode"] = iata_code

if add_iata:
    data_manager.flight_limits = sheet_data
    data_manager.add_iata()

cities_flight_data = []

for city_data in sheet_data:
    city_flight_data = flight_searcher.find_flight(city_data)
    # print(city_flight_data)
    cities_flight_data.append(city_flight_data)
# print(f"flight city data: {type(cities_flight_data)}")
city_prices = flight_data.sort_flight_data(cities_flight_data)
# print("city prices: ", type(city_prices))
print(len(city_prices))
# print(cities_flight_data["data"])
# countries_found = [cities_flight_data["data"][i]["cityTo"] for i in range(len(cities_flight_data["data"]))]
# print(countries_found)
# print(city_prices)
notifications.check_below_limit(sheet_data, city_prices)
