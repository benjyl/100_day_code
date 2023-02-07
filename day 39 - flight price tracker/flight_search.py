import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

FLIGHT_API ="c2hvy6LmveKkQx7e0-p1z-HQG_V9k_9B"
IATA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query" 
FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        pass
    
    def get_IATA_code(self, city):
        # input city and look for top city given, the city code is the IATA code
        params={
            "term": city,
            "location_types": "city",
            "limit": 1
        }
        headers = {
            "apikey": FLIGHT_API
        }
        
        flight_response = requests.get(url=IATA_ENDPOINT, params=params, headers=headers)
        flight_response.raise_for_status()
        flight_response_data = flight_response.json()
        iata_code = flight_response_data["locations"][0]["code"]
        return iata_code
    
    def find_flight(self, cities):
        cities = ",".join(cities)
        print(cities)
        today = datetime.now().strftime("%d/%m/%Y")
        six_months = datetime.now()+relativedelta(months=6)
        six_months = six_months.strftime("%d/%m/%Y")
        print(six_months)
        headers = {
            "apikey": FLIGHT_API
        }
        params = {
            "fly_from": "LON",
            "fly_to": cities,
            "date_from": today,
            "date_to": six_months,
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 7,
            "flight_type": "round",
            "one_for_city": 1,
            "ret_from_diff_city": "False",
            "ret_to_diff_city":"False",
            "selected_cabins": "M",
            "adult_hold_bag": "1",
            "adult_hand_bag": "1",
            "curr": "GBP",
            "max_stopovers":1,
            "limit":10
        }
        flight_response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=params, headers=headers)
        flight_response.raise_for_status()
        flight_response_data = flight_response.json()
        return flight_response_data
       

    