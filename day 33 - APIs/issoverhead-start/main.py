import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import time

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

MY_EMAIL = "jstew613@gmail.com"
PASSWORD = "ioylffhmzmwwrmnq"
RECIP_EMAIL = "benjy.lovat@gmail.com"


def iss_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)

    return abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    return hour_now > sunset or hour_now < sunrise


i = 1
while i < 3:
    # Your position is within +5 or -5 degrees of the ISS position.
    overhead = iss_near()
    print("is overhead: ", overhead)
    print(is_night())

    # If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.

    if iss_near and is_night():
        print("processing")
        message = MIMEText("ISS is overhead now!")
        message["subject"] = "ISS overhead"
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

    print("completed")
    i += 1
    time.sleep(60)
