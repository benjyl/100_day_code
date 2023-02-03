import requests

FLIGHT_API ="c2hvy6LmveKkQx7e0-p1z-HQG_V9k_9B"
FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com/locations/query" 

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
        
        flight_response = requests.get(url=FLIGHT_ENDPOINT, params=params, headers=headers)
        flight_response.raise_for_status()
        flight_response_data = flight_response.json()
        iata_code = flight_response_data["locations"][0]["code"]
        return iata_code
    