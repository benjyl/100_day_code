class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.city_prices = {}

    def sort_flight_data(self, flight_data):
        """
        takes list of flight data from API, extracts city going from, destination,
        flight price and dates
        Args:
            flight_data (list): list of all flight data

        Returns:
            self.city_prices (dict): nested dictionary
        """
        for flight in flight_data:
            if flight is not None:
                # print("flight: ", flight)
                print(flight["cityTo"])
                self.city_prices[f"{flight['cityTo']}"] = {
                    "from": f"{flight['cityFrom']}-{flight['flyFrom']}",
                    "to": f"{flight['cityTo']}-{flight['flyTo']}",
                    "price": flight["price"],
                    "date_from": flight["route"][0]["local_arrival"][:10],
                    "date_to": flight["route"][1]["local_arrival"][:10],
                    "URL": flight["deep_link"],
                }
        return self.city_prices
