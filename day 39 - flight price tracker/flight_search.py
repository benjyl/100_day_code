import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

FLIGHT_API = "c2hvy6LmveKkQx7e0-p1z-HQG_V9k_9B"
IATA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        pass

    def get_IATA_code(self, city):
        """
        Get IATA code for given city
        Args:
            city (string): City interested in getting IATA code for

        Returns:
            iata_code (string): returns the IATA code of the given city
        """
        # input city and look for top city given, the city code is the IATA code
        params = {"term": city, "location_types": "city", "limit": 1}
        headers = {"apikey": FLIGHT_API}

        flight_response = requests.get(
            url=IATA_ENDPOINT, params=params, headers=headers
        )
        flight_response.raise_for_status()
        flight_response_data = flight_response.json()
        iata_code = flight_response_data["locations"][0]["code"]
        return iata_code

    def find_flight(self, city_data):
        """
        Search flight API for flights within next year for the cities given 
        Args:
            city_data (list): list of dictionaries containing city, IATA, price willing to pay
            and row ID of data in google sheets

        Returns:
            flight response data (list): return list of dictionaries, each dictionary containing info of 
            a flight found
        """
        city = city_data["iataCode"]
        today = datetime.now()
        tomorrow = (today + timedelta(days=1)).strftime("%d/%m/%Y")
        next_year = (datetime.now() + relativedelta(years=1)).strftime("%d/%m/%Y")
        headers = {"apikey": FLIGHT_API}
        params = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": tomorrow,
            "date_to": next_year,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            # "ret_from_diff_city": "False",
            # "ret_to_diff_city": "False",
            # "selected_cabins": "M",
            # "adult_hold_bag": "1",
            # "adult_hand_bag": "1",
            "max_stopovers":0,
            "curr": "GBP",

        }
        flight_response = requests.get(
            url=FLIGHT_SEARCH_ENDPOINT, params=params, headers=headers
        )
        flight_response.raise_for_status()
        try:
            flight_response_data = flight_response.json()["data"][0]
            return flight_response_data
        except IndexError:
            print(f"No flight could be found for {city_data['city']}")
        
