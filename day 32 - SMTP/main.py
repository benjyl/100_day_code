import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "jstew613@gmail.com"
PASSWORD = "ioylffhmzmwwrmnq"
RECIP_EMAIL = "jstew613@yahoo.com"

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 2:
    with open("quotes.txt", "r") as file:
        quotes = file.read().splitlines()
        qotd = random.choice(quotes)
        print(qotd)
# method to stop mail going to spam
message = MIMEText(qotd)  # take random quote of the day
message["subject"] = "quote of the day"
message["from"] = MY_EMAIL
message["To"] = RECIP_EMAIL

with smtplib.SMTP(
    "smtp.gmail.com", 587
) as connection:  # 587 - port number to successfully connect for email
    connection.starttls()  # tls (transport layer security-secure connection to email server)
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message.as_string())
"""
# previous method where sent to spam of receiver
with smtplib.SMTP("smtp.gmail.com",587) as connection: # 587 - port number to successfully connect for email
    connection.starttls() # tls (transport layer security-secure connection to email server)
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs=recip_email, 
                        msg=f"Subject: quote of the day\n\n{qotd}")
"""
