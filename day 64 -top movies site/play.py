import requests

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer fb403c26144ea4ee4afd01bfa8444db6"
}

response = requests.get(url="https://api.themoviedb.org/3/movie/550?api_key=fb403c26144ea4ee4afd01bfa8444db6")

print(response.text)