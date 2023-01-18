import smtplib

my_email = "jstew613@gmail.com"
password = "ioylffhmzmwwrmnq"
recip_email = "jstew613@yahoo.com"

with smtplib.SMTP("smtp.gmail.com",587) as connection: # 587 - port number to successfully connect for email
    connection.starttls() # tls (transport layer security-secure connection to email server)
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs=recip_email, 
                        msg="Subject: cricket match\n\nHello this is a test message and not spam")
