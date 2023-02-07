import requests
from datetime import datetime

USERNAME = "benjyl64"
TOKEN = "SDT32dwa45sdf!7*@"
GRAPH = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


headers = {"X-USER-TOKEN": TOKEN}

# create new graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# add pixel

# date = datetime(year=2023, month=1, day=20)
# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
# pixel_config={
#     "date": date.strftime("%Y%m%d"),
#     "quantity": "38.4",
# }
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

# #update a pixel
# date = datetime(year=2023, month=1, day=30)
# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date.strftime('%Y%m%d')}"
# pixel_config={
#     "quantity": "0"
# }

# response = requests.put(url=pixel_update_endpoint, json=pixel_config, headers=headers)

# delete a pixel
date = datetime(year=2023, month=1, day=30)
pixel_delete_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date.strftime('%Y%m%d')}"
)

response = requests.delete(url=pixel_update_endpoint, headers=headers)

print(response.text)
