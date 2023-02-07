from twilio.rest import Client

TWILIO_SID = "AC14cf7f3fe0c4ec44ec2132d3f678fd3e"
AUTH_TOKEN = "20cdb952026b26c67d1c5003bbda28a5"
TWILIO_PHONE = "+19137330970"
MY_PHONE = "+447518778468"


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self) -> None:
        pass

    def check_below_limit(self, sheet_data, flight_data):
        """
        Check whether any flights are below the limts set in google sheets.
        If so, send text with deal, else send text saying no good deals
        Args:
            sheet_data (_type_): _description_
            flight_data (_type_): _description_
        """
        good_deal = False
        for destination in sheet_data:
            
            city = destination["city"]
            max_price = destination["lowestPrice"]
            
            try:
                flight_price = flight_data[city]["price"]
                
            except KeyError:
                print(f"Couldn't find any flight to {city} in this time frame")
                
            else:
                if flight_price < max_price:
                    # print(
                    #     f"Low price alert! Only £{round(flight_price)} to fly from {flight_data[city]['from']} \
                    #       to {flight_data[city]['to']} from {flight_data[city]['date_from']} to {flight_data[city]['date_to']}"
                    # )
                    client = Client(TWILIO_SID, AUTH_TOKEN)
                    message = client.messages.create(
                        body=f"Low price alert! Only £{round(flight_price)} to fly from {flight_data[city]['from']} \
                            to {flight_data[city]['to']} from {flight_data[city]['date_from']} to {flight_data[city]['date_to']}",
                        from_=TWILIO_PHONE,
                        to=MY_PHONE,
                    )
                    good_deal = True
        if not good_deal:
            print("No good deal")
            # client = Client(TWILIO_SID, AUTH_TOKEN)
            # message = client.messages.create(
            #     body=f"No good deals today 😔",
            #     from_=TWILIO_PHONE,
            #     to=MY_PHONE,
            # )
