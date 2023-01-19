import requests
#response codes
# e.g. 404 - doesn't exist 
#1XX: Hold on
#2XX: successful
#3XX: No permission to access 
#4XX: You mucked up
#5XX: Server mucked up e.g. server down
response = requests.get(url="http://api.open-notify.org/iss-now.json") #gets a response code for iss position
response.raise_for_status() # raises exception and explains error for response
# get data from response
data = response.json()
print(data)