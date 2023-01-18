##################### Extra Hard Starting Project ######################
import pandas as pd 
import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "jstew613@gmail.com"
PASSWORD = "ioylffhmzmwwrmnq"

# 1. Update the birthdays.csv
df = pd.read_csv("birthdays.csv")
today = dt.datetime.now()
# print(df["month"])


# 2. Check if today matches a birthday in the birthdays.csv
for (index, row) in df.iterrows():
    # print(row["month"], row["day"])
    # print(today.month, today.day)
    if row["month"] == today.month and row["day"] == today.day:
        person = row

recip_email = person["email"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letter_no = random.randint(1,3)
print(letter_no)
with open(f"./letter_templates/letter_{letter_no}.txt", 'r+') as message:
    bd_wish = message.readlines()
    
personalised = [line.replace("[NAME]", person["name"]) for line in bd_wish]
personalised = "".join(personalised) # Needs to be string for MIMEText to encode it
    
    
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



