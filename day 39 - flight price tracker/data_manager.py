import requests

SHEETY_ENDPOINT = "https://api.sheety.co/b2bfc39b396fc0ac0f35c7b4b25d0fc6/myFlightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.flight_limits = {}
        
    def get_sheet_data(self, testing=True):
        """_summary_

        Returns:
            list: list of json data for each city interested in travelling to
            City name, city IATA code, Lowest price - max price willing to pay 
            for a ticket
        """
        if testing:
            print("Testing, no data to return")
        else:
            data = requests.get(url=SHEETY_ENDPOINT).json()
            # print(data["prices"])
            self.flight_limits = data["prices"]
            print(type(self.flight_limits))
            return self.flight_limits
    
    def add_iata(self):
        """add the IATA code for chosen cities to google doc
        """
        for city in self.flight_limits:
            params={"price":
                {
                "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=params) # id = row number in google sheet
            
        