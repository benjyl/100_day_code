##################### Extra Hard Starting Project ######################
import pandas as pd 
import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "jstew613@gmail.com"
PASSWORD = "ioylffhmzmwwrmnq"


df = pd.read_csv("birthdays.csv")
today = dt.datetime.now()

# Check if today matches a birthday in the birthdays.csv
for (index, row) in df.iterrows():
    if row["month"] == today.month and row["day"] == today.day:
        person = row

recip_email = person["email"]

#pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letter_no = random.randint(1,3)
print(letter_no)
with open(f"./letter_templates/letter_{letter_no}.txt", 'r+') as message:
    bd_wish = message.read() # keeps everything as string

personalised = bd_wish.replace("[NAME]", person["name"])

    
    
# 4. Send the letter generated in step 3 to that person's email address.
message = MIMEText(personalised) 
message["subject"] = "Happy Birthday"
message["from"] = MY_EMAIL
message["To"] = recip_email

with smtplib.SMTP("smtp.gmail.com",587) as connection: # 587 - port number to successfully connect for email
    connection.starttls() # tls (transport layer security-secure connection to email server)
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, 
                        to_addrs=recip_email, 
                        msg=message.as_string())



