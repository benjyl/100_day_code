class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.city_prices = {}

    def sort_flight_data(self, flight_data):
        # print(self.city_prices)
        for flight in flight_data:
            print(flight["cityTo"])
            self.city_prices[f"{flight['cityTo']}"] = {
                "from": f"{flight['cityFrom']}-{flight['flyFrom']}",
                "to": f"{flight['cityTo']}-{flight['flyTo']}",
                "price": flight["price"],
                "date_from": flight["route"][0]["local_arrival"][:10],
                "date_to": flight["route"][1]["local_arrival"][:10],
            }
        return self.city_prices
