import requests
from datetime import datetime

APP_ID = "adbce002"
API_KEY = "27e49ce435ee2dd908ae1a13754df38a"


nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {"query": input("What exercise did you do today?")}

headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
response = requests.post(url=nutrition_endpoint, json=parameters, headers=headers)
response_data = response.json()

# make sure sheet is not in read only mode
sheety_endpoint = (
    "https://api.sheety.co/b2bfc39b396fc0ac0f35c7b4b25d0fc6/myWorkouts/workouts"
)

# headers = {
#     "Authorization": "Basic YmVuanlsNjQ6U0RGXqNGZHNkYWY0NjM0QEFTZWQ=",
#     "Content-Type": "application/json",
# }

for ex in response_data["exercises"]:
    # print(ex["user_input"], ex["duration_min"],ex["nf_calories"])
    sheet_inputs = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.today().strftime("%H:%M:%S"),
            "exercise": ex["user_input"].title(),
            "duration": ex["duration_min"],
            "calories": ex["nf_calories"],
        }
    }
    # sheets_response = requests.post(
    #     url=sheety_endpoint, json=sheet_inputs, headers=headers
    # )
    sheets_response = requests.post(
        url=sheety_endpoint, json=sheet_inputs
    )
    sheets_response.raise_for_status()
