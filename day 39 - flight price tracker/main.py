# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_searcher = FlightSearch()
sheet_data = data_manager.get_sheet_data(testing=False)
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

# sheet_data = [{"city": "Paris", "iataCode": "PAR", "lowestPrice": 200},
#               {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42},
#               {"city": "Tokyo", "iataCode": "TYO","lowestPrice": 485},
#               {"city": "Sydney","iataCode": "SYD", "lowestPrice": 2000},
#               {"city": "Istanbul","iataCode": "IST", "lowestPrice": 95},
#               {"city": "Kuala Lumpur","iataCode": "KUL", "lowestPrice": 1500},
#               {"city": "New York","iataCode": "NYC", "lowestPrice": 1200},
#               {"city": "San Francisco","iataCode": "SFO", "lowestPrice": 260},
#               {"city": "Cape Town","iataCode": "CPT", "lowestPrice": 378},
#               ]

flight_city_data = flight_searcher.find_flight(sheet_data)
print(flight_city_data)
city_prices = flight_data.sort_flight_data(flight_city_data)
print(len(city_prices))
# print(flight_city_data["data"])
# countries_found = [flight_city_data["data"][i]["cityTo"] for i in range(len(flight_city_data["data"]))]
# print(countries_found)
print(city_prices)
notifications.check_below_limit(sheet_data, city_prices)
