import requests

SHEETY_ENDPOINT = (
    "https://api.sheety.co/b2bfc39b396fc0ac0f35c7b4b25d0fc6/myFlightDeals/prices"
)


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        pass

    def get_sheet_data(self, testing=True):
        """_summary_

        Returns:
            list: list of json data for each city interested in travelling to
            City name, city IATA code, Lowest price - max price willing to pay
            for a ticket
        """
        if testing:
            self.flight_limits = [
                {"city": "Paris", "iataCode": "PAR", "lowestPrice": 54, "id": 2},
                {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42, "id": 3},
                {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 485, "id": 4},
                {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 551, "id": 5},
                {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 95, "id": 6},
                {
                    "city": "Kuala Lumpur",
                    "iataCode": "KUL",
                    "lowestPrice": 414,
                    "id": 7,
                },
                {"city": "New York", "iataCode": "NYC", "lowestPrice": 240, "id": 8},
                {
                    "city": "San Francisco",
                    "iataCode": "SFO",
                    "lowestPrice": 260,
                    "id": 9,
                },
                {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 378, "id": 10},
                {"city": "Bali", "iataCode": "DPS", "lowestPrice": 501, "id": 11},
            ]
            return self.flight_limits
        else:
            data = requests.get(url=SHEETY_ENDPOINT).json()
            # print(data["prices"])
            self.flight_limits = data["prices"]
            # print(type(self.flight_limits))
            return self.flight_limits

    def add_iata(self):
        """add the IATA code for chosen cities to google doc"""
        for city in self.flight_limits:
            params = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}", json=params
            )  # id = row number in google sheet
