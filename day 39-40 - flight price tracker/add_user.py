import requests

SHEETY_ENDPOINT = (
    "https://api.sheety.co/b2bfc39b396fc0ac0f35c7b4b25d0fc6/myFlightDeals/users"
)


def add_user(first_name, last_name, email):
    sheet_inputs = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs)
    response.raise_for_status()


print(
    "Welcome to Benjy's Flight Club\nWe find the best flight deals and email you with them."
)
email_match = False
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
while not email_match:
    email_1 = input("what is your email address?\n")
    email_2 = input("Type your email address again\n")
    if email_1 == email_2:
        email_match = True
        add_user(first_name, last_name, email_1)
    else:
        print("Emails do not match please retype them")
