#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_searcher = FlightSearch()
sheet_data = data_manager.get_sheet_data()
print(sheet_data)

add_iata = False # checks if IATA needs to be added to sheet data
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

cities = ["PAR", "BER", "TYO", "SYD", "IST", "KUL", "NYC", "SFO", "CPT"]
flight_data = flight_searcher.find_flight(cities)
print(flight_data["data"])


