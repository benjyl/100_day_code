from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from email.mime.text import MIMEText


# cadence sensor url
PRODUCT_URL="https://www.amazon.co.uk/Wahoo-Cadence-Sensor-Android-Computers/dp/B00L9XNFPY/ref=sr_1_4?crid=1KYRHTU1WSROW&keywords=cadence%2Bsensor&qid=1677591094&sprefix=cade%2Caps%2C93&sr=8-4&th=1"
MY_EMAIL = "jstew613@gmail.com"
PASSWORD = "ioylffhmzmwwrmnq"
RECIP_EMAIL = "benjy.lovat@gmail.com"

def send_email(url, price, product):
    """Send email to me containing product description, price and url
    when price dropped to certain level
    Args:
        url (string): product URL
        price (float): Current product price
        product (float): product name and description
    """
    message = MIMEText(
        f"Price drop found: \nproduct: {product} \ncurrent price: £{price} \nURL: {url}"
    )
    message["subject"] = f"Price alert for {product}"
    message["from"] = MY_EMAIL
    message["To"] = RECIP_EMAIL

    with smtplib.SMTP(
        "smtp.gmail.com", 587
    ) as connection:  # 587 - port number to successfully connect for email
        connection.starttls()  # tls (transport layer security-secure connection to email server)
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=RECIP_EMAIL, msg=message.as_string()
        )



# https://myhttpheader.com/ gives http headers for requests.get

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    }

# headers={"User-Agent": "Defined"}

response = requests.get(url=PRODUCT_URL, headers=headers)
response.raise_for_status()
print(response.text)

soup = BeautifulSoup(response.text, "lxml")
print(soup.title.string) # title of page
product = soup.title.string

# Search amazon on developer tools, price shown in <span class="a-offscreen">
# Strip away £ 
current_price = float(soup.find(class_="a-offscreen").text.strip("£"))
print(current_price)

price_limit = 35

# send self email when item price below limit
if current_price < price_limit:
    send_email(PRODUCT_URL, current_price, product)



