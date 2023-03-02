import requests
from bs4 import BeautifulSoup
 
amz_headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Accept-Language': 'en-US, en;q=0.5'
}
 
amz_url = "https://www.amazon.com/Health-Home-Multifunction-Nonstick-Interchangeable/dp/B0894JVNK7/"
 
response = requests.get(
    url = amz_url,
    headers=amz_headers
).text

# print(response)

soup = BeautifulSoup(response, "html.parser")
print(soup.prettify())
current_price = float(soup.find(class_="a-offscreen").text.strip("$"))
print(current_price)